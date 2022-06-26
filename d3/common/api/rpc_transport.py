from typing import Callable

from pydantic import BaseModel


class RpcSerializer:
    def __init__(self, api_json_handler: Callable[[str, str], str]):
        self.api_json_handler = api_json_handler

    async def send(self, req: BaseModel):
        j = req.json()
        self.api_json_handler(req.__class__.__name__, j)
        print(j)


