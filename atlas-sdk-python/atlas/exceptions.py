

from typing import Any

from attr import s


class AtlasError(Exception):
    """Base exception for all Atlas SDK errors."""


class AtlasAPIError(AtlasError):
    def __init__(
        self,
        message: str,
        *,
        response: Any = None,
    ) -> None:
        super().__init__(message)
        self.response = response
        self.status_code = getattr(response, "status_code", None)


class AtlasAuthenticationError(AtlasAPIError):
    """Raised when API credentials are invalid."""


class AtlasValidationError(AtlasAPIError):
    """Raised when request input is invalid."""


class AtlasNotFoundError(AtlasAPIError):
    """Raised when a requested resource does not exist."""


class AtlasRateLimitError(AtlasAPIError):
    """Raised when the API rate limit is exceeded."""


class AtlasServerError(AtlasAPIError):
    """Raised when Atlas API has a server-side failure."""


class AtlasNetworkError(AtlasError):
    """Raised for network and timeout failures."""