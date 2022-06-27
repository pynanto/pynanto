from app.common.rpc.api_base import ApiBase


class ApiProductRequest(ApiBase):
    a: int
    b: int


class ApiProductResponse(ApiBase):
    product: int


ApiProductRequest.response_type = ApiProductResponse
