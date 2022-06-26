import unittest
from datetime import datetime
from unittest import IsolatedAsyncioTestCase

from d3.common import rpc
from d3.common.api.api_args import ApiSelectionRequest
from d3.common.api.api_base import api_send, api_send_set
from d3.common.api.api_sum import ApiSumRequest, ApiSumResponse
from d3.common.api.rpc_transport import RpcSerializer
from d3.common.api.server_handlers import ServerHandlers
from d3.common.rpc.rpc import Column, DisplayMode


class MyTestCase(IsolatedAsyncioTestCase):

    async def test_rpc(self):
        async def send(req):
            return handle_req(req)

        def handle_req(req: ApiSumRequest):
            return ApiSumResponse(sum=req.a + req.b)

        api_send_set(send)
        req = ApiSumRequest(a=39, b=3)
        res: ApiSumResponse = await req.send()
        self.assertEqual(42, res.sum)

    async def test_rpc_serialized(self):
        def handle_req(req: ApiSumRequest):
            return ApiSumResponse(sum=req.a + req.b)

        server_handlers = ServerHandlers()
        server_handlers.register(handle_req)

        def send_handler(name: str, json_payload: str) -> str:
            # in production this will issue a js `fetch`
            print('name', name, 'json_payload', json_payload)
            return '{}'

        sender = RpcSerializer(send_handler)

        api_send_set(sender.send)
        req = ApiSumRequest(a=39, b=3)
        res: ApiSumResponse = await req.send()
        self.assertEqual(42, res.sum)


if __name__ == '__main__':
    unittest.main()
