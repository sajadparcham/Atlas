

from atlas.config import AtlasConfig
from atlas.resources.responses import ResponsesResource
from atlas.transport.http import HttpTransport


class AtlasClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | None = None,
        timeout: float | None = None,
    ) -> None:
        config = AtlasConfig(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
        )

        self._transport = HttpTransport(config)

        self.responses = ResponsesResource(self._transport)
