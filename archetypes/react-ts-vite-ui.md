# ⚛️ Archetype: React, TypeScript & Vite Frontend

> **Target Domain**: Standalone web applications, interactive dashboards, monitoring portals, and web interfaces with strict layout stability.

---

## 🛠️ Technology Stack

| Layer | Technology | Rationale / Convention |
| :--- | :--- | :--- |
| **Framework & Engine** | React 18+ / TypeScript / Vite | Strict TypeScript (`"strict": true`), fast HMR, optimized bundles. |
| **State Management** | **Zustand** (`use*Store.ts`) | Focused slices, separate files per domain/controller, mandatory granular selectors. |
| **Styling & Theming** | Pure CSS Modules + Custom Properties | Theme tokens in `theme.css`, dark mode support, zero heavy UI bloat. |
| **Data Fetching** | Native `fetch` API wrappers | Lean API clients; avoid heavy TanStack Query unless caching strictly requires it. |
| **Testing & Quality** | Vitest + Playwright + Layout Inspector | Unit tests via Vitest; E2E + 4-point layout audit via `playwright-layout-inspector`. |
| **Linting** | ESLint with Zero Warnings | `eslint . --max-warnings 0` gate in CI. |

---

## 📁 Directory Structure

```
frontend/
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── playwright.config.ts
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── theme.css                 # CSS Custom Properties / Dark Theme
│   ├── components/
│   │   ├── common/               # Button, Modal, Card, Input
│   │   │   ├── Button.tsx
│   │   │   └── Button.module.css
│   │   └── ServerStatus/         # View-oriented component folders
│   │       ├── ServerStatusCard.tsx
│   │       └── ServerStatusCard.module.css
│   ├── hooks/
│   │   └── usePolling.ts
│   ├── stores/
│   │   ├── useServerStore.ts     # Domain-specific Zustand store
│   │   └── useAuthStore.ts
│   └── services/
│       └── apiClient.ts          # Pure fetch API wrapper
└── tests/
    ├── unit/
    │   └── stores.test.ts
    └── e2e/
        ├── navigation.spec.ts
        └── layout-audit.spec.ts  # 4-point layout inspector assertions
```

---

## ⚙️ Zustand Store with Granular Selector Discipline

```typescript
// src/stores/useServerStore.ts
import { create } from 'zustand';

interface ServerModel {
  id: string;
  name: string;
  isOnline: boolean;
}

interface ServerState {
  servers: ServerModel[];
  isLoading: boolean;
  selectedServerId: string | null;
  fetchServers: () => Promise<void>;
  selectServer: (id: string | null) => void;
}

export const useServerStore = create<ServerState>((set) => ({
  servers: [],
  isLoading: false,
  selectedServerId: null,

  fetchServers: async () => {
    set({ isLoading: true });
    try {
      const res = await fetch('/api/servers');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      set({ servers: data, isLoading: false });
    } catch (err) {
      set({ isLoading: false });
      console.error('Failed to fetch servers:', err);
    }
  },

  selectServer: (id) => set({ selectedServerId: id }),
}));

// USAGE IN COMPONENT (Prevents re-renders on unrelated state mutations):
// const serverCount = useServerStore((state) => state.servers.length);
```

---

## 📐 Playwright Layout Inspector Quality Gate

```typescript
// tests/e2e/layout-audit.spec.ts
import { test, expect } from '@playwright/test';
import 'playwright-layout-inspector/matchers';

test.describe('Automated Layout & UX Audit', () => {
  test('audit page across desktop and mobile viewports', async ({ page }) => {
    await page.goto('/');

    // 1. Assert zero horizontal overflow or clipping
    await expect(page).toHaveNoLayoutOverflow();

    // 2. Assert mobile viewport fitting & scaling
    await expect(page).toHaveMobileFit();

    // 3. Assert touch target ergonomics (>= 24px)
    await expect(page).toHaveTouchFriendlyTargets({ minSize: 24 });

    // 4. Assert composite layout score meets Grade A
    await expect(page).toPassLayoutAudit({ minScore: 85 });
  });
});
```
