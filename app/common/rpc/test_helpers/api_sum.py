from app.common.rpc.api_base import ApiBase


class ApiSumResponse(ApiBase):
    sum: int


class ApiSumRequest(ApiBase):
    response_type = ApiSumResponse
    a: int
    b: int
