---
title: "Simulation & Control Harnesses"
description: "Observable dynamic systems, diagnostic tap points, parameter sweeps, and 6-part feedback envelopes."
---

# 🧪 Simulation & Control Harnesses: Observation, Testing & Feedback for Developers and AI

This guide defines the simulation architecture, test harness conventions, and closed-loop verification practices that ensure software stability, deterministic performance, and $\ge$ 80% code coverage.

---

## 🎯 1. Software as an Observable Dynamic System

A controls and modeling/simulation background approaches software as a **closed-loop dynamic system**:
1. **Observable States**: Systems expose internal states through diagnostic tap points, metrics, and health probes.
2. **High-Volume & Parameter Sweeps**: Test harnesses simulate high-throughput stress, batch processing, and parameter sweeps to evaluate numeric stability and boundary limits.
3. **Disturbance Ingestion**: Systems process imperfect inputs, synthetic latency, and abrupt disconnects to prove graceful recovery.
4. **Closed-Loop Feedback**: Tests capture state responses, compute deltas, and return structured diagnostic envelopes for rapid developer and AI self-correction.

```mermaid
flowchart TD
    subgraph T1["Tier 1: Inner Loop (On Demand)"]
        Unit["Fast Unit Tests<br>In-memory, isolated domain logic assertions"]
    end
    subgraph T2["Tier 2: Stabilization Gate (Pre-Manual)"]
        Integ["Targeted Integration Tests<br>Boundary contracts & provider mocks"]
    end
    subgraph T3["Tier 3: Quality Gate (Pre-PR / Pre-Release / CI)"]
        Matrix["Pairwise & Multi-Provider Matrix"]
        Sim["Simulation Harnesses & Stress Loops"]
        E2E["Playwright Layout Inspector & E2E"]
        Smoke["Fullstack Smoke Gate"]
    end

    T1 -->|Interfaces Stabilize| T2
    T2 -->|Manual Verification Passes| T3
    Matrix --> Sim --> E2E --> Smoke
```

---

## ⏱️ 2. Tiered Testing Cadence ("Test When It Makes Sense")

Running slow or brittle integration suites during rapid prototyping stalls development momentum. Use a tiered cadence to balance iteration speed with system reliability:

### 2.1 Tier 1: Inner Loop / Rapid Development
- Execute fast, isolated in-memory unit tests on demand.
- Do not mandate test runs while exploring early drafts, prototypes, or rapidly changing contracts.
- Focus on fast feedback for core algorithms, data transformations, and pure functions.

### 2.2 Tier 2: Stabilization Gate / Pre-Manual Verification
- Trigger once feature interfaces, API signatures, and data boundaries stabilize.
- Run unit test suites and targeted integration tests immediately before manual testing.
- Catch contract breakages and regressions before spending human or agent verification time.

### 2.3 Tier 3: Pre-PR / Pre-Release / CI Quality Gate
- Run full test matrix, multi-provider integration suites, and simulation harnesses.
- Execute Playwright layout audits across mobile and desktop viewports.
- Enforce the $\ge$ 80% code coverage target and verify zero warnings.
- Block merges into `develop` or `main` until all gate stages pass cleanly.

---

## 🏗️ 3. When to Build a Dedicated Simulation Harness

Build a dedicated simulation harness whenever:
1. **Crossing an Architectural Boundary**: An external API, database, child process STDIO, SSE stream, or network protocol enters the architecture.
2. **Implementing Tunable Algorithms**: Logic has variability, numeric convergence, thresholding, sorting, or scoring that requires parameter sweeping.
3. **Stateful Protocols & Daemons**: Systems use background workers, queue consumers (`Channel<T>`), or multi-step transaction pipelines.

---

## ⚙️ 4. Harness Types & Simulation Patterns

### 4.1 High-Volume & Stress Loop Harness
Wrap the component under test in a high-volume execution loop feeding batches of synthetic or recorded inputs:

```csharp
// Example: High-Volume C# Closed-Loop Harness
public class HighVolumeSimulationHarness
{
    private readonly IProcessingEngine _engine;

    public async Task<HarnessResult> RunBatchAsync(int batchSize, CancellationToken ct)
    {
        var transitions = new List<StateTransition>();
        var sw = Stopwatch.StartNew();

        for (int i = 0; i < batchSize; i++)
        {
            var payload = GenerateSyntheticPayload(i);
            var result = await _engine.ProcessAsync(payload, ct);
            transitions.Add(new StateTransition(i, result.State, sw.ElapsedMilliseconds));
        }

        return new HarnessResult(batchSize, transitions, sw.Elapsed);
    }
}
```

### 4.2 Synthetic Mock Transports (`mock_stdio.js`)
Simulate child process STDIO with controllable latency, stdout buffering, stderr emission, and abrupt process termination:

```javascript
// mock_stdio.js - Simulates asynchronous JSON-RPC communication & disconnects
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: false });

rl.on('line', (line) => {
  try {
    const req = JSON.parse(line);
    if (req.method === 'trigger_disconnect') {
      process.exit(1); // Abrupt crash to test reconnection
    }
    setTimeout(() => {
      if (req.method === 'ping') {
        console.log(JSON.stringify({ jsonrpc: '2.0', id: req.id, result: 'pong' }));
      }
    }, 50);
  } catch (err) {
    process.stderr.write(`Malformed JSON: ${line}\n`);
  }
});
```

### 4.3 Disturbance Injection
Inject failures specifically to test error fallbacks and graceful degradation:
- **Malformed Payloads**: Ingest corrupt JSON, truncated strings, and invalid encodings.
- **Abrupt Disconnects**: Terminate child processes or socket streams mid-handshake to verify `CancellationToken` cleanup and retry logic.
- **Latency Spikes**: Inject artificial delays to verify timeout thresholds and circuit breakers.

---

## 🔍 5. Diagnostic Tap Points & Agent Introspection

### Development Tap Point Protocol
During development and debugging:
1. **Inject Hooks**: Inject internal diagnostic hooks (e.g. event subscriptions, state snapshot getters, in-memory ring buffers).
2. **Inspect Internals**: Test harnesses subscribe to these hooks to assert internal state transitions without relying on unstructured log parsing.
3. **Clean Up**: Remove or compile-guard debug hooks before production release.

---

## 📐 6. UI Layout Stability & Ergonomics Auditing

Frontends integrate **`playwright-layout-inspector`** with `data-testid` attributes to catch visual regressions and accessibility defects:

```typescript
import { test, expect } from '@playwright/test';
import 'playwright-layout-inspector/matchers';

test.describe('Responsive Layout & Ergonomics Audit', () => {
  test('audit page layout across viewports', async ({ page }) => {
    await page.goto('/');

    // 1. Assert zero unwanted horizontal scrollbars or element bleed
    await expect(page).toHaveNoLayoutOverflow();

    // 2. Assert mobile viewport & zoom readiness
    await expect(page).toHaveMobileFit();

    // 3. Assert touch targets meet WCAG standards (>= 24px)
    await expect(page).toHaveTouchFriendlyTargets({ minSize: 24 });

    // 4. Assert overall layout UX score is Grade A
    await expect(page).toPassLayoutAudit({ minScore: 85 });
  });
});
```

---

## 📋 7. The 6-Part Agent Feedback Envelope

When a test harness, integration test, or simulation loop fails, the failure output MUST be packaged in a standardized diagnostic envelope:

```json
{
  "status": "FAILED",
  "test_name": "Test_HighThroughput_OrderBatch_Convergence",
  "inputs": {
    "batch_size": 1000,
    "concurrency_limit": 16,
    "seed": 42
  },
  "assumptions": [
    "Database connection pool size >= 20",
    "Channel buffer capacity >= 500"
  ],
  "active_settings": {
    "journal_mode": "WAL",
    "synchronous": "NORMAL",
    "busy_timeout": 5000
  },
  "action_history": [
    { "step": 1, "action": "SpawnWorkerPool", "status": "OK" },
    { "step": 2, "action": "Enqueue500Items", "status": "OK" },
    { "step": 3, "action": "SimulateDisconnect", "status": "TRIGGERED" },
    { "step": 4, "action": "DrainChannel", "status": "TIMEOUT" }
  ],
  "output_delta": {
    "expected_processed": 500,
    "actual_processed": 482,
    "unprocessed_delta": 18
  },
  "captured_logs": [
    "ERROR [Worker-3] CancellationTokenSource timed out after 5000ms",
    "WARN [Pool] Connection dropped during transaction commit"
  ],
  "reproduction_command": "dotnet test --filter \"FullyQualifiedName=Harness.Test_HighThroughput\" -- --seed 42"
}
```
