# 🏛️ Archetype: C# Console & CLI Application

> **Target Domain**: High-performance command-line utilities, background daemons, developer tools, batch workers, and protocol runners.

---

## 🛠️ Technology Stack

| Layer | Technology | Rationale / Convention |
| :--- | :--- | :--- |
| **Runtime & Language** | .NET 9 / C# 13 | `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, `.slnx` format. |
| **CLI Framework** | `System.CommandLine` or `CommandLineParser` | Robust argument parsing, verb/subcommand dispatching, type validation. |
| **Dependency Injection** | `Microsoft.Extensions.Hosting` | Full `IHost` / `HostApplicationBuilder`, `Microsoft.Extensions.DependencyInjection`. |
| **Logging & Output** | `ILogger` + `--json` Output Stream | Human-friendly console logs + structured JSON mode for agent consumption. |
| **Packaging & Binary** | Framework-Dependent + Native AOT Ready | `<PublishAot>` compatibility for instant startup when required. |
| **Persistence** | SQLite WAL / Dapper (if required) | `IDbConnectionFactory`, stored procedure `.sql` files. |
| **Testing** | xUnit + NSubstitute | Simulation test harnesses with mock process STDIO and cancellation token tests. |

---

## 📁 Directory Structure

```
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

## ⚙️ Core Implementation Patterns

### 1. Program.cs & Host Builder
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

## 🔍 Diagnostic Tap Points & Agent Flags

Every CLI tool must support standard agent inspection flags:
1. **`--json`**: Emits raw JSON objects to `stdout` for autonomous agent parsing.
2. **`--dry-run`**: Validates parameters, queries external state, and simulates processing without destructive writes.
3. **`-v / -vv / -vvv`**: Increases logging verbosity and dumps internal ring buffer diagnostics upon failure.
