from app.common.api.api_square import ApiSquareRequest, ApiSquareResponse


def handle(req: ApiSquareRequest) -> ApiSquareResponse:
    return ApiSquareResponse(square=req.x * req.x)
