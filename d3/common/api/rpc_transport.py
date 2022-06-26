import json
from typing import Callable

from pydantic import BaseModel


class RpcSend:
    def __init__(self, api_json_handler: Callable[[str, str], str]):
        self.api_json_handler = api_json_handler

    async def send(self, req: BaseModel):
        request_json = req.json()
        response_json = self.api_json_handler(req.__class__.__name__, request_json)
        response_args = json.loads(response_json)
        response = req.response_class(**response_args)
        return response

