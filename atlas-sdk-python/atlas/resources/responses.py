

from atlas.models.responses import Response
from atlas.transport.http import HttpTransport


class ResponsesResource:
    def __init__(self, transport: HttpTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        model: str,
        input: str,
        temperature: float | None = None,
    ) -> Response:
        payload = {
            "model": model,
            "input": input,
        }

        if temperature is not None:
            payload["temperature"] = temperature

        data = self._transport.request(
            "POST",
            "/responses",
            json=payload,
        )

        return Response.from_dict(data)
