# 🏛️ Architecture: {{PROJECT_NAME}}

This document details the high-level architecture, module boundaries, data flows, and concurrency/security guarantees of **{{PROJECT_NAME}}**.

---

## 🏗️ High-Level System Architecture

```mermaid
flowchart TD
    subgraph Clients["Clients & Agents"]
        Browser["Web UI (React 19 / Vite 8)"]
        Agent["AI Agent / Automated Client"]
    end

    subgraph API["API & Middleware Layer"]
        MinimalAPI["ASP.NET Core Minimal APIs (.NET 10)"]
        AuthMiddleware["Authentication & Validation Middleware"]
    end

    subgraph Core["Core Business Logic"]
        SliceA["Components/FeatureA"]
        SliceB["Components/FeatureB"]
    end

    subgraph Persistence["Data Persistence Layer"]
        DbFactory["DbConnectionFactory (SQLite WAL / MS SQL / MySQL)"]
        Dapper["Dapper Query Engine"]
        Database[("SQLite WAL Database")]
    end

    Browser --> MinimalAPI
    Agent --> MinimalAPI
    MinimalAPI --> AuthMiddleware
    AuthMiddleware --> SliceA
    AuthMiddleware --> SliceB
    SliceA --> Dapper
    SliceB --> Dapper
    Dapper --> DbFactory
    DbFactory --> Database
```

---

## 📡 Message & Request Sequence Flow

```mermaid
sequenceDiagram
    autonumber
    actor User as Client / User
    participant Frontend as React SPA (Zustand)
    participant API as Minimal API (.NET 10)
    participant Repo as Dapper Repository
    participant DB as SQLite WAL Database

    User->>Frontend: Trigger User Action
    Frontend->>API: HTTP POST /api/items (JSON Payload)
    API->>API: Validate Input & Check CancellationToken
    API->>Repo: CreateAsync(request, ct)
    Repo->>DB: INSERT INTO Items (Id, Name, CreatedAtUtc) VALUES (...)
    DB-->>Repo: Acknowledge Write
    Repo-->>API: Return ItemModel
    API-->>Frontend: HTTP 201 Created (Item JSON)
    Frontend-->>User: Optimistic UI Update in Store
```

---

## 🧩 Modular Boundaries & Structure

```text
├── Components/         # Feature vertical slices (Endpoints, Models, Repositories)
├── Infrastructure/     # Persistence (DbConnectionFactory, Seeders), Logging, Transports
├── Core/               # Domain interfaces, Exceptions, Thread-safe State wrappers
└── tests/              # xUnit Unit & Pairwise Integration Tests
```

---

## 📐 Non-Functional Requirements & Design Guarantees

1. **Deterministic Latency**: Sub-millisecond local in-memory queries and WAL database reads.
2. **Concurrency Safety**: Lock-free or `ConcurrentDictionary` state wrappers; `CancellationToken` wired across all async operations.
3. **Data Integrity**: Parameterized SQL queries preventing injection; zero heavy ORM overhead.
4. **UX Ergonomics**: Frontends audited using `playwright-layout-inspector` to guarantee responsive viewport fit without horizontal overflow.
