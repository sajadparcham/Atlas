

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    id: str
    model: str
    output_text: str
    raw: dict[str, Any]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Response":
        return cls(
            id=data["id"],
            model=data["model"],
            output_text=data.get("output_text", ""),
            raw=data,
        )
