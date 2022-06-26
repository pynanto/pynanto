from d3.common.api.api_product import ApiProductRequest, ApiProductResponse


def handle(req: ApiProductRequest) -> ApiProductResponse:
    return ApiProductResponse(product=req.a * req.b)
