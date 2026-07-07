API_NAME_SEARCH = "api_search"
API_NAME_ADD_SERVICE = "api_add_service"
API_ENDPOINT = "http://www.deepnlp.org/api/ai_agent_marketplace/v1"
MOCK_ACCESS_KEY = "${your_access_key}"

DEFAULT_TIMEOUT = 5
DEFAULT_SEARCH_LIMIT = 100

REQUIRED_REGISTRY_FIELDS = ("content",)
OPTIONAL_REGISTRY_FIELDS = (
    "website",
    "field",
    "subfield",
    "content_tag_list",
    "github",
    "price",
    "api",
    "thumbnail_picture",
    "upload_image_files",
)
