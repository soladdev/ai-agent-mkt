import json
import logging
import os
import sys

logger = logging.getLogger(__name__)


def _data_file_path(filename: str) -> str:
    if sys.version_info < (3, 9):
        from importlib_resources import files
    else:
        from importlib.resources import files

    return os.path.join(str(files("ai_agent_marketplace.data")), filename)


def load_mock_json(filename: str) -> dict:
    """Load bundled mock JSON data for offline demos."""
    try:
        path = _data_file_path(filename)
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        logger.error("Failed to load mock data from %s: %s", filename, exc)
        return {}


def get_mock_search_result() -> dict:
    return load_mock_json("search_api_demo.json")


def get_mock_addservice_result() -> dict:
    return load_mock_json("add_service_api_demo.json")
