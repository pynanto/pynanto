from datetime import datetime
from typing import Tuple, Optional, List

from app.common.rpc.api_base import ApiBase


class ApiSelectionResponse(ApiBase):
    timestamp_values: List[datetime]


class ApiSelectionRequest(ApiBase):
    response_type = ApiSelectionResponse
    window: Optional[Tuple[datetime, datetime]]
