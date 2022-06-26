from d3.common.rpc.api_base import ApiBase


class ApiBadRequest(ApiBase):
    ignore: str


class ApiBadResponse(ApiBase):
    ignore: str

    # this request is missing
    # ApiBadRequest.response_class = ApiBadResponse


def wrong_handler(req: ApiBadRequest) -> ApiBadResponse:
    pass
