import unittest
from unittest import IsolatedAsyncioTestCase

from pydantic import BaseModel

from d3.common.rpc.api_base import api_send_set
from d3.common.rpc.test_helpers.api_sum import ApiSumRequest, ApiSumResponse
from d3.common.rpc.rpc_handlers import RpcHandlers
from d3.common.rpc.rpc_send import RpcSend
from d3.common.rpc.test_helpers.bad_api import ApiBadRequest


class MyTestCase(IsolatedAsyncioTestCase):

    async def test_rpc(self):
        async def send(req) -> BaseModel:
            return handle_req(req)

        def handle_req(req: ApiSumRequest):
            return ApiSumResponse(sum=req.a + req.b)

        api_send_set(send)
        req = ApiSumRequest(a=39, b=3)
        res: ApiSumResponse = await req.send()
        self.assertEqual(42, res.sum)

    async def test_rpc_serialized(self):
        def handle_req(req: ApiSumRequest) -> ApiSumResponse:
            return ApiSumResponse(sum=req.a + req.b)

        server_handlers = RpcHandlers()
        server_handlers.register(handle_req)

        async def send_handler(name: str, json_payload: str) -> str:
            # in production this will issue a js `fetch`
            return server_handlers.dispatch_str(name, json_payload)

        sender = RpcSend(send_handler)

        api_send_set(sender.send)

        req = ApiSumRequest(a=39, b=3)
        res: ApiSumResponse = await req.send()
        self.assertEqual(42, res.sum)

    async def test_send_of_wrong_request(self):
        req = ApiBadRequest(ignore='ignore')

        def send_handler(name: str, json_payload: str) -> str:
            raise Exception('should not be called')

        sender = RpcSend(send_handler)
        try:
            await sender.send(req)
        except Exception as ex:
            print(ex)
            return

        self.fail('No exception!')


if __name__ == '__main__':
    unittest.main()
