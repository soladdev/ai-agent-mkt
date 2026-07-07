"""Backward-compatible re-exports. Prefer importing from ai_agent_marketplace directly."""

from .client import AddServiceAPI, BaseAPI, SearchFunctionAPI
from .client.mock import get_mock_addservice_result, get_mock_search_result
from .constants import API_ENDPOINT as API_AI_AGENT_MARKETPLACE_ENDPOINT
from .constants import MOCK_ACCESS_KEY

__all__ = [
    "BaseAPI",
    "SearchFunctionAPI",
    "AddServiceAPI",
    "get_mock_search_result",
    "get_mock_addservice_result",
    "API_AI_AGENT_MARKETPLACE_ENDPOINT",
    "MOCK_ACCESS_KEY",
]
