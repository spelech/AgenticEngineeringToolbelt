# 🐍 Archetype: Python FastAPI & FastMCP Service (APIs First, MCP Later)

> **Architect**: Steven T. Pelech  
> **Target Domain**: Scrapers, data pipelines, computer vision, AI/ML workflows, automation engines, and native Model Context Protocol (MCP) servers.  
> **Core Principle**: **APIs First, MCP Later** — Domain logic, schemas, and endpoints live in typed, self-contained APIs first; MCP tools act strictly as thin wrappers.

---

## 🔌 1. Architectural Philosophy: APIs First, MCP Later

1. **APIs First**:
   - Design and implement domain models, validation, and business logic inside self-contained core engines and typed FastAPI endpoints.
   - All capabilities must be fully testable via standard unit tests and HTTP client calls without requiring an MCP client.
2. **MCP Later**:
   - Expose Model Context Protocol (MCP) server tools as lightweight wrapper functions delegating directly to the underlying domain engine or internal API services.
   - Do not embed proprietary domain logic, database queries, or unvalidated state transformations directly inside MCP tool handlers.
3. **Dual Accessibility**:
   - The service is simultaneously consumable by human developers / web frontends via OpenAPI/REST and by autonomous AI agents via FastMCP (SSE / Streamable HTTP / STDIO).

---

## 🛠️ 2. Technology Stack

| Layer | Technology | Rationale / Convention |
| :--- | :--- | :--- |
| **Runtime & Package Manager** | Python 3.12+ / `uv` | Modern `pyproject.toml` managed with ultra-fast `uv`. |
| **API & Web Framework** | FastAPI + Uvicorn | High-performance asynchronous REST API with automatic OpenAPI docs. |
| **Agent Tooling (MCP)** | FastMCP / MCP SDK | Native Streamable HTTP / SSE / STDIO Model Context Protocol endpoint wrapping domain APIs. |
| **Data Validation & Settings** | Pydantic v2 + `pydantic-settings` | Strict typing, immutable schemas, environment & `.env` parsing. |
| **CLI & Commands** | Typer | Type-hint driven CLI interface reusing Pydantic models. |
| **Persistence** | SQLite / `aiosqlite` / async SQLAlchemy | Async relational access, clean schema migrations. |
| **Testing & Quality** | `pytest` + `pytest-asyncio` + `ruff` | $\ge$ 80% coverage via `pytest-cov`, zero linter errors via `ruff`. |

---

## 📁 3. Directory Structure

```
my_service/
├── pyproject.toml
├── README.md
├── ARCHITECTURE.md
├── Dockerfile
├── docker-compose.yaml
├── src/
│   └── my_service/
│       ├── __init__.py
│       ├── config.py                 # Pydantic Settings
│       ├── main.py                   # FastAPI App Lifecycle & MCP Mounting
│       ├── cli.py                    # Typer CLI Entrypoint
│       ├── core/
│       │   ├── models.py             # Pydantic Domain Schemas
│       │   ├── exceptions.py         # Domain Exceptions
│       │   └── engine.py             # Core Domain Business Logic (Engine)
│       ├── api/                      # APIs First: Typed REST Endpoints
│       │   ├── router.py             # API Router Aggregator
│       │   └── v1/
│       │       └── endpoints.py      # REST Endpoints calling core.engine
│       ├── mcp/                      # MCP Later: Thin Tool Wrappers
│       │   ├── server.py             # FastMCP Instance & Setup
│       │   └── tools.py              # Thin FastMCP Wrappers calling core.engine
│       └── infrastructure/
│           ├── database.py           # aiosqlite / Session Factory
│           └── taps.py               # Diagnostic Hooks & Ring Buffer
└── tests/
    ├── conftest.py
    ├── test_unit_core.py             # Tier 1: Core domain logic tests
    ├── test_api_endpoints.py         # Tier 1: FastAPI endpoint tests
    ├── test_mcp_wrappers.py          # Tier 1/2: FastMCP wrapper tests
    └── test_simulation_harness.py    # Tier 2: Simulation loop & disturbance tests
```

---

## ⚙️ 4. FastMCP Integration Pattern (APIs First, MCP Later)

```python
"""Example demonstrating APIs First, MCP Later architectural pattern."""

from fastapi import FastAPI, APIRouter, HTTPException, Depends
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# ============================================================================
# 1. CORE DOMAIN: Models & Engine (APIs First)
# ============================================================================

class ProcessRequest(BaseModel):
    item_id: str = Field(..., description="Target entity identifier")
    dry_run: bool = Field(False, description="Simulate execution without persisting changes")

class ProcessResult(BaseModel):
    item_id: str
    status: str
    processed: bool
    details: str

class DomainEngine:
    """Core domain business logic decoupled from transport protocols."""
    async def execute_processing(self, request: ProcessRequest) -> ProcessResult:
        if not request.item_id:
            raise ValueError("item_id cannot be empty")
        # Perform actual domain computation or workflow
        return ProcessResult(
            item_id=request.item_id,
            status="completed",
            processed=True,
            details="Successfully processed via domain engine"
        )

engine = DomainEngine()

# ============================================================================
# 2. REST API: First-Class FastAPI Endpoints
# ============================================================================

api_router = APIRouter(prefix="/api/v1")

@api_router.post("/process", response_model=ProcessResult)
async def process_endpoint(request: ProcessRequest) -> ProcessResult:
    """Primary REST API endpoint for human developers and frontend clients."""
    try:
        return await engine.execute_processing(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

# ============================================================================
# 3. MCP ADAPTER: Lightweight FastMCP Wrappers (MCP Later)
# ============================================================================

mcp = FastMCP("my_service", instructions="Provides domain processing tools")

@mcp.tool()
async def process_entity(request: ProcessRequest) -> dict:
    """Agent tool wrapping the core domain engine cleanly."""
    result = await engine.execute_processing(request)
    return result.model_dump()

# ============================================================================
# 4. APP LIFECYCLE: Composed FastAPI + FastMCP Server
# ============================================================================

app = FastAPI(title="My Service API", version="1.0.0")
app.include_router(api_router)
mcp.mount(app, prefix="/mcp")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```

---

## 🧪 5. Testing Cadence

- **Tier 1 (Inner Loop)**: Unit tests for `core/engine.py`, Pydantic models, and FastAPI `TestClient` route tests.
- **Tier 2 (Stabilization Gate)**: Integration tests validating FastMCP tool execution, diagnostic tap points, and synthetic simulation loops.
- **Tier 3 (CI / Release)**: Multi-stage CI pipeline, ruff linter gate (0 errors), and $\ge$ 80% coverage threshold.
