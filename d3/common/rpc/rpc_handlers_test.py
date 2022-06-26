import json
import unittest

from d3.common.rpc.api_base import ApiBase
from d3.common.rpc.test_helpers.api_sum import ApiSumRequest, ApiSumResponse
from d3.common.rpc.rpc_handlers import RpcHandlers
from d3.common.rpc.test_helpers.bad_api import wrong_handler


class MyTestCase(unittest.TestCase):

    def test_wrong_reg(self):
        def wrong_1(req):
            pass

        def wrong_2(req: int):
            pass

        def wrong_3(req: ApiBase):
            pass

        def wrong_4(req: ApiSumRequest):
            pass

        def wrong_5(req: ApiSumRequest) -> int:
            pass

        def wrong_6(req: ApiSumRequest) -> ApiBase:
            pass

        should_be = self.register_should_raise
        should_be(wrong_1)
        should_be(wrong_2)
        should_be(wrong_3)
        should_be(wrong_4)
        should_be(wrong_5)
        should_be(wrong_6)

    def test_wrong_request_definition(self):
        self.register_should_raise(wrong_handler)

    def test_register_and_dispatch(self):
        target = RpcHandlers()
        request = ApiSumRequest(a=39, b=3)
        response = ApiSumResponse(sum=42)

        def sum_handler(req: ApiSumRequest) -> ApiSumResponse:
            self.assertEqual(req, request)
            return response

        target.register(sum_handler)

        actual = target.dispatch(request)

        self.assertEqual(response, actual)

    def test_no_handler(self):
        target = RpcHandlers()
        request = ApiSumRequest(a=39, b=3)

        self.assertRaises(Exception, target.dispatch, request)

    def test_dispatch_json(self):
        target = RpcHandlers()

        def sum_handler(req: ApiSumRequest) -> ApiSumResponse:
            return ApiSumResponse(sum=req.a + req.b)

        target.register(sum_handler)

        resp_json = target.dispatch_str(ApiSumRequest.__name__, ApiSumRequest(a=39, b=3).json())
        response = ApiSumResponse(**json.loads(resp_json))
        self.assertEqual(42, response.sum)

    def register_should_raise(self, fun):
        try:
            RpcHandlers().register(fun)
        except Exception as ex:
            print(fun.__name__, ex)
            return
        self.fail('Did not raise exception')


if __name__ == '__main__':
    unittest.main()
