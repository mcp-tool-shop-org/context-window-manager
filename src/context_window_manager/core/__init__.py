"""
Core components for Context Window Manager.

This package contains the foundational infrastructure:
- SessionRegistry: Session and window metadata management
- KVStore: KV cache storage abstraction
- VLLMClient: vLLM server communication
- WindowManager: Orchestration of freeze/thaw operations
"""

from context_window_manager.core.kv_store import (
    BlockMetadata,
    CacheMetrics,
    DiskKVStore,
    KVStoreBackend,
    MemoryKVStore,
    RetrieveResult,
    StorageBackend,
    StoreResult,
    TieredKVStore,
    compute_block_hash,
    create_kv_store,
)
from context_window_manager.core.session_registry import (
    Session,
    SessionRegistry,
    SessionState,
    Window,
)
from context_window_manager.core.vllm_client import (
    CacheStats,
    ChatMessage,
    ChatResponse,
    GenerateResponse,
    ModelInfo,
    VLLMClient,
)
from context_window_manager.core.window_manager import (
    AutoFreezeManager,
    AutoFreezePolicy,
    AutoFreezeResult,
    CacheInfo,
    CloneResult,
    FreezeResult,
    ThawResult,
    WarmCacheResult,
    WindowManager,
)

__all__ = [
    # KV Store
    "BlockMetadata",
    "CacheMetrics",
    "DiskKVStore",
    "KVStoreBackend",
    "MemoryKVStore",
    "RetrieveResult",
    "StorageBackend",
    "StoreResult",
    "TieredKVStore",
    "compute_block_hash",
    "create_kv_store",
    # Session Registry
    "Session",
    "SessionRegistry",
    "SessionState",
    "Window",
    # vLLM Client
    "CacheStats",
    "ChatMessage",
    "ChatResponse",
    "GenerateResponse",
    "ModelInfo",
    "VLLMClient",
    # Window Manager
    "AutoFreezeManager",
    "AutoFreezePolicy",
    "AutoFreezeResult",
    "CacheInfo",
    "CloneResult",
    "FreezeResult",
    "ThawResult",
    "WarmCacheResult",
    "WindowManager",
]
