from d3.common.rpc.api_base import ApiBase


class ApiSumRequest(ApiBase):
    a: int
    b: int


class ApiSumResponse(ApiBase):
    sum: int


ApiSumRequest.response_type = ApiSumResponse
