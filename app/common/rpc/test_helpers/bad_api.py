from app.common.rpc.api_base import ApiBase


class ApiBadResponse(ApiBase):
    ignore: str


class ApiBadRequest(ApiBase):
    # this request is missing
    # response_class = ApiBadResponse
    ignore: str


def wrong_handler(req: ApiBadRequest) -> ApiBadResponse:
    pass
