from app.common.rpc.api_base import ApiBase


class ApiSquareResponse(ApiBase):
    square: int


class ApiSquareRequest(ApiBase):
    response_type = ApiSquareResponse
    x: int

