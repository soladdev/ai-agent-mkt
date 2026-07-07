"""AI Agent Marketplace — search and registry client for DeepNLP."""

import logging

from .__version__ import __version__
from .client import AddServiceAPI, SearchFunctionAPI
from .utils import function_to_schema, function_to_schema_claude

__all__ = [
    "__version__",
    "search",
    "add",
    "SearchFunctionAPI",
    "AddServiceAPI",
    "function_to_schema",
    "function_to_schema_claude",
]

logger = logging.getLogger(__name__)


def search(q, **kwargs):
    """Search the AI Agent Marketplace index.

    Args:
        q: Search query string. An empty query returns bundled demo data.
        limit: Maximum number of results (default 100).
        timeout: Request timeout in seconds (default 5).

    Returns:
        dict: Search results from the marketplace API.
    """
    api = SearchFunctionAPI()
    try:
        return api.api(q, **kwargs)
    except Exception as exc:
        logger.exception("Search failed: %s", exc)
        return {}


def add(access_key, name, item_info, **kwargs):
    """Register an AI agent in the marketplace.

    Args:
        access_key: API key from https://www.deepnlp.org/workspace/keys
        name: Display name for the agent.
        item_info: Agent metadata dict (must include ``content``).
        timeout: Request timeout in seconds (default 5).

    Returns:
        dict: Registration response from the marketplace API.
    """
    api = AddServiceAPI()
    try:
        return api.api(access_key, name, item_info, **kwargs)
    except Exception as exc:
        logger.exception("Registration failed: %s", exc)
        return {}
