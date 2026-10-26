# Software Requirements Specification: {{PROJECT_NAME}}

This specification defines the functional requirements, category taxonomy, and automated test traceability matrix for **{{PROJECT_NAME}}**.

---

## Requirement Category Taxonomy

Requirement identifiers use `<CATEGORY>-<NN>` format (`AUTH-01`, `DB-01`, `GUARD-01`, `MCP-01`, `SEC-01`, `TRANS-01`, `UI-01`). Do not use generic `REQ-` prefixes.

| Category Code | Domain Scope | Proof Types |
| :--- | :--- | :--- |
| **`AUTH`** | Authentication, SSO, RBAC, and session lifecycle | `PositiveFeature` / `FailClosedGuardrail` |
| **`DB`** | Schema migrations, SQLite WAL / SQL persistence, encryption at rest | `PositiveFeature` / `FailClosedGuardrail` |
| **`GUARD`** | Fail-closed guardrails, rate limits, timeout/cancellation bounds | `FailClosedGuardrail` |
| **`MCP`** | Model Context Protocol tool routing, schema validation, SSE/HTTP transport | `PositiveFeature` / `FailClosedGuardrail` |
| **`SEC`** | Secret redaction, subprocess sanitization, input validation | `FailClosedGuardrail` |
| **`TRANS`** | Upstream/downstream protocol bridges, HTTP/MQTT transport resilience | `PositiveFeature` / `FailClosedGuardrail` |
| **`UI`** | Responsive layout geometry, theme tokens, interactive user journeys | `PositiveFeature` |

---

## Requirements and Traceability Matrix

| Requirement ID | Category | Type | Summary | Acceptance Criteria | Automated Test Proof |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`TRANS-01`** | `TRANS` | `PositiveFeature` | **Health Check Probe** | Exposes `/health` returning HTTP 200 with service status and version JSON. | `Backend.Tests/HealthEndpointsTests.cs::HealthEndpoint_ReturnsOk` |
| **`DB-01`** | `DB` | `PositiveFeature` | **Item Persistence CRUD** | Valid requests persist records in SQLite WAL and return HTTP 201. | `Backend.Tests/ItemEndpointsTests.cs::CreateItem_ValidRequest_ReturnsCreated` |
| **`GUARD-01`** | `GUARD` | `FailClosedGuardrail` | **Invalid Payload Rejection** | Empty or malformed payloads fail closed with HTTP 400 and structured error details. | `Backend.Tests/ItemEndpointsTests.cs::CreateItem_EmptyName_ReturnsBadRequest` |
| **`MCP-01`** | `MCP` | `PositiveFeature` | **MCP Adapter Routing** | Namespaced MCP tool calls delegate to the underlying domain service. | `Backend.Tests/McpToolTests.cs::CallTool_ListItems_ReturnsDomainPayload` |
| **`UI-01`** | `UI` | `PositiveFeature` | **Responsive Layout Audit** | Primary views pass the 4-point Playwright layout audit with zero horizontal overflow. | `frontend/e2e/layout.spec.ts::dashboard passes layout inspection` |

---

## Requirement Definitions

### `TRANS-01`: Health Check Probe
- **Category**: `TRANS` (`PositiveFeature`)
- **Description**: Provide an unauthenticated `/health` probe endpoint for container orchestrators and uptime monitors returning `{"status": "healthy", "version": "<semver>"}`.
- **Verification**: In-process HTTP integration test via `WebApplicationFactory` or `httpx.AsyncClient`.

### `DB-01`: Item Persistence CRUD
- **Category**: `DB` (`PositiveFeature`)
- **Description**: Persist domain entities using parameterized queries or stored procedures against SQLite WAL (`PRAGMA journal_mode = WAL;`) with full `CancellationToken` propagation.
- **Verification**: Repository integration test against a real ephemeral SQLite database.

### `GUARD-01`: Invalid Payload Rejection
- **Category**: `GUARD` (`FailClosedGuardrail`)
- **Description**: Reject invalid inputs at the API boundary with typed validation error envelopes and zero leaked stack traces.
- **Verification**: Boundary (`0-1-N`) and disturbance test assertions.

### `MCP-01`: MCP Adapter Routing
- **Category**: `MCP` (`PositiveFeature`)
- **Description**: Expose domain operations over `/mcp` and `/sse` using thin MCP wrapper tools (`<serverId>__<toolName>`).
- **Verification**: In-process MCP session client roundtrip test.

### `UI-01`: Responsive Layout Audit
- **Category**: `UI` (`PositiveFeature`)
- **Description**: Render desktop (`1920x1080`) and mobile (`390x844`) viewports with zero horizontal overflow, touch targets `≥ 24px`, and composite layout score `≥ 85`.
- **Verification**: `playwright-layout-inspector` automated 4-point audit.
