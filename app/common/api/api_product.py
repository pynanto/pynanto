from app.common.rpc.api_base import ApiBase


class ApiProductResponse(ApiBase):
    product: int


class ApiProductRequest(ApiBase):
    response_type = ApiProductResponse
    a: int
    b: int
