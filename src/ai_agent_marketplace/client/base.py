class BaseAPI:
    """Base class for AI Agent Marketplace API clients."""

    def __init__(self, configs=None):
        self.configs = configs

    def api(self, *args, **kwargs):
        raise NotImplementedError
