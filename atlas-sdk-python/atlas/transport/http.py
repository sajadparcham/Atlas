

from typing import Any

import httpx

from atlas.config import AtlasConfig
from atlas.exceptions import (
    AtlasAuthenticationError,
    AtlasNotFoundError,
    AtlasRateLimitError,
    AtlasServerError,
    AtlasValidationError,
    AtlasNetworkError,
)


class HttpTransport:
    def __init__(self, config: AtlasConfig) -> None:
        self._client = httpx.Client(
            base_url=config.base_url,
            timeout=config.timeout,
            headers={
                "Authorization": f"Bearer {config.api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "atlas-python/0.1.0",
            },
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        try:
            response = self._client.request(
                method=method,
                url=path,
                json=json,
                params=params,
            )
        except httpx.TimeoutException as exc:
            raise AtlasNetworkError(
                "The request to Atlas timed out."
            ) from exc
        except httpx.RequestError as exc:
            raise AtlasNetworkError(
                "Could not connect to the Atlas API."
            ) from exc

        self._raise_for_status(response)

        if response.status_code == 204:
            return {}

        return response.json()

    def close(self) -> None:
        self._client.close()

    def _raise_for_status(self, response: httpx.Response) -> None:
        if 200 <= response.status_code < 300:
            return

        try:
            body = response.json()
        except ValueError:
            body = {}

        message = body.get("message") or body.get("error") or response.text

        if response.status_code == 401:
            raise AtlasAuthenticationError(message, response=response)

        if response.status_code == 404:
            raise AtlasNotFoundError(message, response=response)

        if response.status_code in (400, 422):
            raise AtlasValidationError(message, response=response)

        if response.status_code == 429:
            raise AtlasRateLimitError(message, response=response)

        if response.status_code >= 500:
            raise AtlasServerError(message, response=response)

        response.raise_for_status()
