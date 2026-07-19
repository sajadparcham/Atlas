

from dataclasses import dataclass


@dataclass(frozen=True)
class AtlasConfig:
    api_key: str
    base_url: str | None = None
    timeout: float | None = None

    def __post_init__(self) -> None:
        if not self.api_key or not self.api_key.strip():
            raise ValueError("api_key must not be empty")

        if self.base_url is None:
            object.__setattr__(
                self,
                "base_url",
                "https://api.atlas.example/v1",
            )

        if self.timeout is None:
            object.__setattr__(self, "timeout", 30.0)

        if self.timeout <= 0:
            raise ValueError("timeout must be greater than zero")
