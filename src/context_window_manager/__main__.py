"""
Entry point for the Context Window Manager MCP server.

Usage:
    python -m context_window_manager
    cwm  # If installed via pip
"""

import asyncio
import sys
from multiprocessing import freeze_support


def main() -> int:
    """Main entry point."""
    # Windows multiprocessing support
    freeze_support()

    from context_window_manager.server import run_server

    try:
        asyncio.run(run_server())
        return 0
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
