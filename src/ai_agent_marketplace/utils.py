"""Backward-compatible re-exports. Prefer ai_agent_marketplace.utils."""

from .utils.schema import function_to_schema, function_to_schema_claude

__all__ = ["function_to_schema", "function_to_schema_claude"]
