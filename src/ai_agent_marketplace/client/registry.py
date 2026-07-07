import logging

import requests

from ..constants import (
    API_ENDPOINT,
    API_NAME_ADD_SERVICE,
    DEFAULT_TIMEOUT,
    MOCK_ACCESS_KEY,
    OPTIONAL_REGISTRY_FIELDS,
    REQUIRED_REGISTRY_FIELDS,
)
from .base import BaseAPI
from .mock import get_mock_addservice_result

logger = logging.getLogger(__name__)


class AddServiceAPI(BaseAPI):
    """Client for registering agents in the AI Agent Marketplace."""

    def __init__(self, configs=None):
        super().__init__(configs)
        self.name = API_NAME_ADD_SERVICE
        self.base_request_uri = API_ENDPOINT
        self.keys_required = list(REQUIRED_REGISTRY_FIELDS)
        self.keys_optional = list(OPTIONAL_REGISTRY_FIELDS)
        self.KEY_PAGE_URL = "url"
        self.timeout = DEFAULT_TIMEOUT

    def api(self, access_key, name, item_info, **kwargs):
        if access_key == MOCK_ACCESS_KEY:
            logger.debug(
                "Mock access key detected; returning demo response. "
                "Register at http://www.deepnlp.org/workspace/my_ai_services"
            )
            return get_mock_addservice_result()

        input_param = {
            "access_key": access_key,
            "content_name": name,
        }

        for key in self.keys_required:
            if key not in item_info:
                logger.error("Required field '%s' missing from item_info", key)
                return {}
            input_param[key] = item_info[key]

        filled_fields = []
        missing_fields = []
        for key in self.keys_optional:
            if key in item_info:
                input_param[key] = item_info[key]
                filled_fields.append(key)
            else:
                missing_fields.append(key)

        logger.debug(
            "Optional registry fields filled=%s missing=%s",
            filled_fields,
            missing_fields,
        )

        timeout = kwargs.get("timeout", self.timeout)
        if not isinstance(timeout, int):
            timeout = self.timeout

        try:
            response = requests.post(
                self.base_request_uri,
                data=input_param,
                timeout=timeout,
            )
            if response.status_code == 200:
                data = response.json()
                agent_url = data.get(self.KEY_PAGE_URL, "")
                logger.info("Agent registered successfully: %s", agent_url)
                return data

            logger.warning(
                "Registry request failed with status %s",
                response.status_code,
            )
        except requests.RequestException as exc:
            logger.error("Registry request failed: %s", exc)

        return {}
