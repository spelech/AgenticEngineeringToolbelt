# Archetype: Python FastAPI and FastMCP Service

> **Architect**: Steven T. Pelech  
> **Target Domain**: Scrapers, data pipelines, computer vision, AI/ML workflows, automation engines, and native Model Context Protocol (MCP) servers.  
> **Core Principle**: **APIs First, MCP Later** — Domain logic, schemas, and endpoints live in typed, self-contained APIs first; MCP tools act strictly as thin wrappers.

---

## Architectural Philosophy: APIs First, MCP Later

### Core Domain APIs First

- Design and implement domain models, validation, and business logic inside self-contained core engines and typed FastAPI endpoints (see [APIs First, MCP Later](../standards/ENGINEERING_STYLE_GUIDE.md#apis-first-mcp-later)).
- Verify all capabilities through standard unit tests and HTTP client roundtrips without requiring an MCP runtime.

### Thin MCP Wrappers Second

- Expose Model Context Protocol (MCP) server tools as lightweight wrapper functions that delegate directly to the underlying domain engine or internal API services.
- Never embed proprietary domain logic, raw database queries, or unvalidated state mutations inside MCP tool handlers.
- Serve human developers and web frontends via OpenAPI/REST while simultaneously serving AI agents via FastMCP (Streamable HTTP, SSE, or STDIO).

---

## Technology Stack

| Layer | Technology | Rationale and Convention |
| :--- | :--- | :--- |
| **Runtime & Package Manager** | Python 3.12+ / `uv` | Modern `pyproject.toml` managed with fast `uv`. |
| **API & Web Framework** | FastAPI + Uvicorn | High-performance asynchronous REST API with automatic OpenAPI documentation. |
| **Agent Tooling (MCP)** | FastMCP / MCP SDK | Native Streamable HTTP, SSE, and STDIO Model Context Protocol endpoints wrapping domain APIs. |
| **Data Validation & Settings** | Pydantic v2 + `pydantic-settings` | Strict typing, immutable schemas, and environment / `.env` parsing. |
| **CLI & Commands** | Typer | Type-hint driven CLI interface reusing Pydantic models. |
| **Persistence** | SQLite / `aiosqlite` / async SQLAlchemy | Asynchronous relational access and clean schema migrations. |
| **Testing & Quality** | `pytest` + `pytest-asyncio` + `ruff` | **≥ 80% coverage** via `pytest-cov` and zero linter errors via `ruff`. |

---

## Directory Structure

```text
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

## FastMCP Integration Pattern

```python
"""Example demonstrating APIs First, MCP Later architectural pattern."""

from fastapi import FastAPI, APIRouter, HTTPException
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# 1. Core Domain: Models & Engine (APIs First)
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
        return ProcessResult(
            item_id=request.item_id,
            status="completed",
            processed=True,
            details="Successfully processed via domain engine"
        )

engine = DomainEngine()

# 2. REST API: First-Class FastAPI Endpoints
api_router = APIRouter(prefix="/api/v1")

@api_router.post("/process", response_model=ProcessResult)
async def process_endpoint(request: ProcessRequest) -> ProcessResult:
    """Primary REST API endpoint for human developers and frontend clients."""
    try:
        return await engine.execute_processing(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

# 3. MCP Adapter: Lightweight FastMCP Wrappers (MCP Later)
mcp = FastMCP("my_service", instructions="Provides domain processing tools")

@mcp.tool()
async def process_entity(request: ProcessRequest) -> dict:
    """Agent tool wrapping the core domain engine cleanly."""
    result = await engine.execute_processing(request)
    return result.model_dump()

# 4. App Lifecycle: Composed FastAPI + FastMCP Server
app = FastAPI(title="My Service API", version="1.0.0")
app.include_router(api_router)
mcp.mount(app, prefix="/mcp")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```

---

## Testing Cadence and Representative Recipes

Follow the [Tiered Testing Cadence](../standards/TESTING_HARNESS_PATTERNS.md#tiered-testing-cadence) and use real transports instead of synthetic mocks (see [Python FastAPI and FastMCP Harness Recipes](../standards/TESTING_HARNESS_PATTERNS.md#python-3-12-fastapi-and-fastmcp)):
- **Tier 1 (Inner Loop)**: Unit tests for `core/engine.py`, Pydantic models, and fast ASGI in-memory route tests.
- **Tier 2 (Stabilization Gate)**: Integration tests validating FastMCP tool execution via `InMemorySessionClient`, diagnostic tap points, and synthetic simulation loops.
- **Tier 3 (CI & Release)**: Multi-stage CI pipeline, `ruff` linter gate (0 errors), and **≥ 80% coverage** threshold.

### ASGI In-Memory Transport with SQLite

Test FastAPI endpoints through asynchronous HTTP roundtrips using `httpx.AsyncClient` with `ASGITransport(app=app)` against an ephemeral SQLite database. Never patch internal domain logic with `unittest.mock.patch`:

```python
import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app
from app.database import init_db

@pytest.fixture
async def client(tmp_path):
    test_db = f"sqlite+aiosqlite:///{tmp_path}/test.db"
    await init_db(test_db)
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
```

### FastMCP In-Memory Session Client

Test FastMCP tools through `InMemorySessionClient` to exercise live tool execution and validate structured output schemas:

```python
import pytest
from mcp.client.inmemory import InMemorySessionClient
from app.mcp_server import mcp

@pytest.mark.asyncio
async def test_mcp_tool_execution():
    async with InMemorySessionClient(mcp) as session:
        result = await session.call_tool("calculate_metrics", arguments={"sample_rate": 100})
        assert result.content[0].text is not None
        assert "convergence_score" in result.content[0].text
```
