from d3.common.api.api_base import ApiBase


class ApiSumRequest(ApiBase):
    a: int
    b: int


class ApiSumResponse(ApiBase):
    sum: int
