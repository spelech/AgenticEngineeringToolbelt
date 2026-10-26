---
title: "Archetype: .NET Console & CLI"
description: "Production-grade CLI utilities with System.CommandLine, dependency injection, and subprocess test harnesses."
---

# Archetype: C# Console and CLI Application

> **Target Domain**: High-performance command-line utilities, background daemons, developer tools, batch workers, and protocol runners.

---

## Technology Stack

| Layer | Technology | Rationale and Convention |
| :--- | :--- | :--- |
| **Runtime & Language** | .NET 10 / C# 13 | `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, `.slnx` format. |
| **CLI Framework** | `System.CommandLine` or `CommandLineParser` | Robust argument parsing, verb and subcommand dispatching, and type validation. |
| **Dependency Injection** | `Microsoft.Extensions.Hosting` | Full `IHost` / `HostApplicationBuilder` and `Microsoft.Extensions.DependencyInjection`. |
| **Logging & Output** | `ILogger` + `--json` Output Stream | Human-friendly console logs plus structured JSON mode for agent consumption. |
| **Packaging & Binary** | Framework-Dependent + Native AOT Ready | `<PublishAot>` compatibility for instant startup when required. |
| **Persistence** | SQLite WAL / Dapper (if required) | `IDbConnectionFactory` and stored procedure `.sql` files (see [Relational Persistence and SQLite WAL](/standards/engineering-style-guide#relational-persistence-and-sqlite-wal)). |
| **Testing** | xUnit + Subprocess Fixtures | Simulation harnesses with real subprocess execution and `CancellationToken` verification. |

---

## Directory Structure

```text
MyCliTool/
├── MyCliTool.slnx
├── Directory.Build.props
├── src/
│   └── MyCliTool/
│       ├── MyCliTool.csproj
│       ├── Program.cs
│       ├── Commands/
│       │   ├── RootCommandDef.cs
│       │   ├── ProcessBatchCommand.cs
│       │   └── DiagnosticsCommand.cs
│       ├── Core/
│       │   ├── Interfaces/
│       │   │   ├── IBatchProcessor.cs
│       │   │   └── IDiagnosticTap.cs
│       │   ├── Models/
│       │   └── Services/
│       │       └── BatchProcessorService.cs
│       └── Infrastructure/
│           ├── Logging/
│           └── Taps/
│               └── DiagnosticRingBuffer.cs
└── tests/
    └── MyCliTool.Tests/
        ├── MyCliTool.Tests.csproj
        ├── Unit/
        └── Simulation/
            └── BatchProcessorHarnessTests.cs
```

---

## Core Implementation Patterns

### Host Builder and Command Wiring

Wire services through `Host.CreateApplicationBuilder` and register global inspection flags on `RootCommand`:

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System.CommandLine;

var builder = Host.CreateApplicationBuilder(args);

// Register Core Services & Commands
builder.Services.AddSingleton<IBatchProcessor, BatchProcessorService>();
builder.Services.AddSingleton<IDiagnosticTap, DiagnosticRingBuffer>();
builder.Services.AddTransient<ProcessBatchCommand>();

using var host = builder.Build();

// Configure System.CommandLine
var rootCommand = new RootCommand("High-performance CLI utility");
var jsonOption = new Option<bool>("--json", "Emit output in machine-readable JSON format");
var dryRunOption = new Option<bool>("--dry-run", "Simulate execution without modifying state");
var verboseOption = new Option<int>("-v", () => 0, "Verbosity level (1-3)");

rootCommand.AddGlobalOption(jsonOption);
rootCommand.AddGlobalOption(dryRunOption);
rootCommand.AddGlobalOption(verboseOption);

// Bind subcommands
var processCmd = host.Services.GetRequiredService<ProcessBatchCommand>().Build();
rootCommand.AddCommand(processCmd);

return await rootCommand.InvokeAsync(args);
```

---

## Diagnostic Tap Points and Agent Flags

Support three standard agent inspection flags on every CLI tool (see [Diagnostic Tap Points](/standards/testing-harness-patterns#diagnostic-tap-points-and-agent-introspection)):
1. **`--json`**: Emits structured JSON objects to `stdout` for autonomous agent parsing.
2. **`--dry-run`**: Validates parameters, queries external state, and simulates processing without destructive writes.
3. **`-v / -vv / -vvv`**: Increases logging verbosity and dumps internal ring-buffer diagnostics upon failure.

---

## Representative Subprocess Test Harness

### CLI Execution Fixture

Test CLI commands through real subprocess execution inside an isolated temporary workspace directory. Never mock command handlers or argument parsers directly (see [C# Fullstack and CLI Harness Recipes](/standards/testing-harness-patterns#c-net-10-fullstack-and-cli)):

```csharp
public class CliExecutionHarness : IDisposable
{
    public string TempWorkspace { get; } = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());

    public CliExecutionHarness() => Directory.CreateDirectory(TempWorkspace);

    public async Task<(int ExitCode, string StdOut, string StdErr)> ExecuteAsync(params string[] args)
    {
        var psi = new ProcessStartInfo("dotnet", string.Join(" ", args))
        {
            WorkingDirectory = TempWorkspace,
            RedirectStandardOutput = true,
            RedirectStandardError = true
        };
        using var proc = Process.Start(psi)!;
        var stdout = await proc.StandardOutput.ReadToEndAsync();
        var stderr = await proc.StandardError.ReadToEndAsync();
        await proc.WaitForExitAsync();
        return (proc.ExitCode, stdout, stderr);
    }

    public void Dispose() => Directory.Delete(TempWorkspace, recursive: true);
}
```

### Verification Guidelines

- Assert expected process exit codes (`0` for success, non-zero for handled errors).
- Assert machine-readable `stdout` payloads when the `--json` flag is supplied.
- Assert expected filesystem mutations inside `TempWorkspace`.
- Verify error handling with invalid arguments, simulated timeouts, and non-zero exit codes.
