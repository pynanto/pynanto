import json
from typing import Callable, Awaitable

from pydantic import BaseModel

from app.common.rpc.api_base import ApiBase


class RpcSend:
    def __init__(self, api_json_handler: Callable[[str, str], Awaitable[str]]):
        self.api_json_handler = api_json_handler

    async def send(self, req: BaseModel):
        request_type = req.__class__
        ApiBase.check_request_completeness(request_type)
        request_json = req.json()
        response_json = await self.api_json_handler(request_type.__name__, request_json)
        response_args = json.loads(response_json)
        response = request_type.response_type(**response_args)
        return response
