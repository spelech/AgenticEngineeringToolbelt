# 🐍 Archetype: Python FastAPI & FastMCP Service

> **Target Domain**: Scrapers, data pipelines, computer vision, AI/ML workflows, automation engines, and native Model Context Protocol (MCP) servers.

---

## 🛠️ Technology Stack

| Layer | Technology | Rationale / Convention |
| :--- | :--- | :--- |
| **Runtime & Package Manager** | Python 3.12+ / `uv` | Modern `pyproject.toml` managed with ultra-fast `uv`. |
| **API & Web Framework** | FastAPI + Uvicorn | High-performance asynchronous REST API with automatic OpenAPI docs. |
| **Agent Tooling (MCP)** | FastMCP / MCP SDK | Native Streamable HTTP / SSE / STDIO Model Context Protocol endpoint. |
| **Data Validation & Settings** | Pydantic v2 + `pydantic-settings` | Strict typing, immutable schemas, environment & `.env` parsing. |
| **CLI & Commands** | Typer | Type-hint driven CLI interface reusing Pydantic models. |
| **Persistence** | SQLite / `aiosqlite` / async SQLAlchemy | Async relational access, clean schema migrations. |
| **Testing & Quality** | `pytest` + `pytest-asyncio` + `ruff` | $\ge$ 80% coverage via `pytest-cov`, zero linter errors via `ruff`. |

---

## 📁 Directory Structure

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
│       ├── config.py             # Pydantic Settings
│       ├── main.py               # FastAPI App & Lifecycle
│       ├── cli.py                # Typer CLI Entrypoint
│       ├── core/
│       │   ├── models.py         # Pydantic Domain Models
│       │   ├── exceptions.py     # Domain Exceptions
│       │   └── engine.py         # Business Engine
│       ├── mcp/
│       │   ├── server.py         # FastMCP Tool Definitions
│       │   └── tools.py
│       └── infrastructure/
│           ├── database.py       # aiosqlite / Session Factory
│           └── taps.py           # Diagnostic Hooks & Ring Buffer
└── tests/
    ├── conftest.py
    ├── test_unit.py
    ├── test_mcp_tools.py
    └── test_simulation_harness.py
```

---

## ⚙️ FastMCP Integration Pattern

```python
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize FastMCP Server
mcp = FastMCP("my_service", instructions="Provides domain processing tools")

class ProcessRequest(BaseModel):
    item_id: str = Field(..., description="Target entity ID")
    dry_run: bool = Field(False, description="Simulate without mutating")

@mcp.tool()
async def process_entity(request: ProcessRequest) -> dict:
    """Process a target entity through the pipeline."""
    # Execute domain logic cleanly
    return {"status": "success", "item_id": request.item_id, "processed": True}

# Mount on FastAPI application
app = FastAPI(title="My Service API")
mcp.mount(app, prefix="/mcp")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```
