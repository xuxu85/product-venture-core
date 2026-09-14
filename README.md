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

## Current execution path

The first Finder worker is the existing `product-opportunity-finder-skill`:

`AronLEEdev/product-opportunity-finder-skill`

It is executed as a Claude Skill using Claude-in-Chrome against real Amazon data, with Helium 10 as an optional/recommended enrichment lane. The Core does not duplicate that browser workflow. The adapter in `adapters/finder_opportunity.py` converts the completed Finder report into the Core `AgentResult` contract.

Target first run:

`Amazon.es → Beverage → Water → Electrolyte Water`

The workflow may continue in degraded mode when H10 is unavailable if the Finder can produce sufficient real Amazon evidence. H10 is not purchased or activated merely to satisfy the architecture. If the next gate genuinely requires a provider credential or paid metric, execution stops at that exact dependency and records the specific missing metric/function before any capital decision.

## Current scope

v0.1: reusable core skeleton extracted from the `product-engine` laboratory repository, plus the minimum Finder/Pain interfaces and Finder-output adapter needed to execute the first real cycle. Concrete provider integrations are added only when a real bottleneck is proven.
