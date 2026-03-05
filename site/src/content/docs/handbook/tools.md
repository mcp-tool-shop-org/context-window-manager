---
title: MCP Tools
description: Six operations for managing context windows.
sidebar:
  order: 2
---

## Core operations

| Tool | Description |
|------|-------------|
| `window_freeze` | Snapshot session context to persistent storage |
| `window_thaw` | Restore context from a saved window |
| `window_list` | List all available context windows |
| `window_status` | Get detailed session and window info |
| `window_clone` | Branch a context for parallel exploration |
| `window_delete` | Remove a saved window and free storage |

## Usage

```bash
# Freeze your current session
> window_freeze session_abc123 my-coding-project

# Later, restore it exactly as it was
> window_thaw my-coding-project

# Branch for exploration
> window_clone my-coding-project my-project-v2

# Check status
> window_status my-coding-project

# List all saved windows
> window_list
```
