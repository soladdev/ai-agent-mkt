import logging
from urllib.parse import urlencode

import requests

from ..constants import (
    API_ENDPOINT,
    API_NAME_SEARCH,
    DEFAULT_SEARCH_LIMIT,
    DEFAULT_TIMEOUT,
)
from .base import BaseAPI
from .mock import get_mock_search_result

logger = logging.getLogger(__name__)


class SearchFunctionAPI(BaseAPI):
    """Client for the AI Agent Marketplace search endpoint."""

    def __init__(self, configs=None):
        super().__init__(configs)
        self.name = API_NAME_SEARCH
        self.base_request_uri = API_ENDPOINT
        self.timeout = DEFAULT_TIMEOUT
        self.limit_default = DEFAULT_SEARCH_LIMIT

    def api(self, q, **kwargs):
        if not q:
            logger.debug("Empty query; returning mock search result")
            return get_mock_search_result()

        limit = kwargs.get("limit", self.limit_default)
        timeout = kwargs.get("timeout", self.timeout)

        if not isinstance(limit, int):
            limit = self.limit_default
        if not isinstance(timeout, int):
            timeout = self.timeout

        params = {"q": q, "limit": limit}
        url = f"{self.base_request_uri}?{urlencode(params)}"

        try:
            logger.debug("Searching marketplace: %s", url)
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return response.json()
            logger.warning("Search request failed with status %s", response.status_code)
        except requests.RequestException as exc:
            logger.error("Search request failed for %s: %s", url, exc)

        return {}
