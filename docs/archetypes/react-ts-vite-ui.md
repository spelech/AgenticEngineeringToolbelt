---
title: "Archetype: React TS Vite UI"
description: "React 19, TypeScript, Zustand, TailwindCSS, and Playwright layout audits."
---

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

## 🧪 Representative Test Harness: Playwright E2E & Layout Audit

Execute realistic operator user journeys against live running frontend applications. Do not write shallow component tests that mock sub-components with empty `<div>` tags. Avoid fragile DOM snapshot testing. Validate user inputs, state transitions, and visible DOM changes. Combine functional interaction checks with the mandatory 4-point layout inspector audit:
1. Zero horizontal layout overflow (`toHaveNoLayoutOverflow`).
2. Mobile viewport fit (`toHaveMobileFit`).
3. Touch target ergonomics ($\ge$ 24px) (`toHaveTouchFriendlyTargets`).
4. Composite layout quality score ($\ge$ 85) (`toPassLayoutAudit`).

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
