---
title: "Archetype: React TS Vite UI"
description: "React 19, TypeScript, Zustand, CSS Modules, and Playwright layout audits."
---

# Archetype: React, TypeScript, and Vite Frontend

> **Target Domain**: Standalone web applications, interactive dashboards, monitoring portals, and web interfaces with strict layout stability.

---

## Technology Stack

| Layer | Technology | Rationale and Convention |
| :--- | :--- | :--- |
| **Framework & Engine** | React 18+ / TypeScript / Vite | Strict TypeScript (`"strict": true`), fast HMR, and optimized bundles (see [Frontend Architecture](/standards/engineering-style-guide#frontend-architecture)). |
| **State Management** | **Zustand** (`use*Store.ts`) | Focused slices, separate files per domain or controller, and mandatory granular selectors. |
| **Styling & Theming** | Pure CSS Modules + Custom Properties | Theme tokens in `theme.css`, dark mode support, and zero heavy UI library bloat. |
| **Data Fetching** | Native `fetch` API wrappers | Lean API clients; avoid heavy external query libraries unless complex caching requires them. |
| **Testing & Quality** | Vitest + Playwright + Layout Inspector | Unit tests via Vitest; end-to-end and 4-point layout audit via `playwright-layout-inspector`. |
| **Linting** | ESLint with Zero Warnings | `eslint . --max-warnings 0` gate enforced in CI. |

---

## Directory Structure

```text
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

## Zustand Store with Granular Selector Discipline

Partition state into dedicated domain store files and subscribe with granular selector functions to prevent unnecessary component re-renders (see [Zustand State and Granular Selectors](/standards/engineering-style-guide#zustand-state-and-granular-selectors)):

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

## Representative Test Harness: Playwright and Layout Audit

### Four-Point Layout Audit Requirements

Execute realistic operator user journeys against live running frontend applications. Do not write shallow component tests that mock child components with empty `<div>` tags or rely on fragile DOM snapshots. Combine functional interaction assertions with the 4-point `playwright-layout-inspector` audit (see [UI Layout Stability and Ergonomics Auditing](/standards/testing-harness-patterns#ui-layout-stability-and-ergonomics-auditing)):
1. **Zero Horizontal Overflow**: `toHaveNoLayoutOverflow()`
2. **Mobile Viewport Fit**: `toHaveMobileFit()`
3. **Touch Target Ergonomics (≥ 24px)**: `toHaveTouchFriendlyTargets({ minSize: 24 })`
4. **Composite Layout Score (≥ 85)**: `toPassLayoutAudit({ minScore: 85 })`

### Playwright User Journey Recipe

```typescript
// tests/e2e/order-journey.spec.ts
import { test, expect } from '@playwright/test';
import 'playwright-layout-inspector/matchers';

test.describe('Order Management User Journey', () => {
  test('operator can submit order and view updated table', async ({ page }) => {
    await page.goto('/');

    await page.getByTestId('sku-input').fill('SKU-999');
    await page.getByTestId('quantity-input').fill('10');
    await page.getByTestId('submit-order-btn').click();

    const row = page.getByTestId('order-row-SKU-999');
    await expect(row).toBeVisible();
    await expect(row.getByTestId('order-status')).toHaveText('Pending');

    // 4-Point Ergonomics & Layout Audit
    await expect(page).toHaveNoLayoutOverflow();
    await expect(page).toHaveMobileFit();
    await expect(page).toHaveTouchFriendlyTargets({ minSize: 24 });
    await expect(page).toPassLayoutAudit({ minScore: 85 });
  });
});
```
