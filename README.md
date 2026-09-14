# Product Venture Core

Minimal reusable execution skeleton for the Product Venture.

## Purpose

Connect ready-made agents, workflows, tools, and data providers to a stable pipeline without rebuilding existing research or marketplace infrastructure.

**Primary metric:** TIME → FIRST REAL SALE

This repository is not an Amazon database, scraper, review platform, Product Intelligence Engine, sourcing marketplace, or autonomous capital allocator.

## Architecture

```text
READY-MADE TOOLS / AGENTS / DATA
        ↓
      ADAPTERS
        ↓
   PRODUCT VENTURE CORE
   ├── contracts
   ├── state
   ├── gates
   ├── policy
   └── router
        ↓
     STAGES
   FINDER → PAIN → OPPORTUNITY → PRODUCT THESIS → VALIDATION
        ↓
      BUILDER / SELLER
```

## Rules

- Reuse existing mechanisms first.
- Core owns contracts, routing, state, and gate policy.
- Agents execute work; they do not authorize capital.
- Providers are replaceable behind adapters.
- Missing evidence is not a PASS.
- Every important thesis has an invalidation condition.
- Do not add infrastructure unless required for the next decision gate.

## Current scope

v0.1: reusable core skeleton extracted from the `product-engine` laboratory repository. Concrete marketplace/data integrations are added only when a real bottleneck is proven.
