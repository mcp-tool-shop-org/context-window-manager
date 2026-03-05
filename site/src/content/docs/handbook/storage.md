---
title: Storage & Architecture
description: Tiered storage, session isolation, and production readiness.
sidebar:
  order: 3
---

## Storage tiers

CWM automatically manages storage across tiers:

1. **CPU Memory** — Fast, limited capacity
2. **Disk** — Large capacity, compressed
3. **Redis** — Distributed, shared across instances

Promotion and demotion between tiers is automatic. Fast restore when warm, reliable restore when cold, shared restore with Redis.

## Session isolation

Each session gets a unique `cache_salt`, ensuring:

- No cross-session data leakage
- Protection against timing attacks
- Clean separation between concurrent contexts

## Production status

- **366 tests** — full async coverage with pytest-asyncio, property-based tests via Hypothesis
- **7 completed phases** — from core infrastructure through integration and polish
- **vLLM + LMCache stack** — built on proven inference infrastructure

## Development

```bash
git clone https://github.com/mcp-tool-shop-org/context-window-manager
cd context-window-manager
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/unit/
```
