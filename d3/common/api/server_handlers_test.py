import unittest

from d3.common.api.api_base import ApiBase
from d3.common.api.api_sum import ApiSumRequest, ApiSumResponse
from d3.common.api.server_handlers import ServerHandlers


class MyTestCase(unittest.TestCase):
    def test_wrong_reg(self):
        def shouldRaise(fun):
            try:
                ServerHandlers().register(fun)
                self.fail('Did not raise exception')
            except Exception as ex:
                print(fun.__name__, ex)

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

        shouldRaise(wrong_1)
        shouldRaise(wrong_2)
        shouldRaise(wrong_3)
        shouldRaise(wrong_4)
        shouldRaise(wrong_5)
        shouldRaise(wrong_6)

    def test_ok(self):
        target = ServerHandlers()

        def sum_handler(req: ApiSumRequest) -> ApiSumResponse:
            pass

        target.register(sum_handler)


if __name__ == '__main__':
    unittest.main()
