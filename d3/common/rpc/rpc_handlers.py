import inspect
import json
from dataclasses import dataclass
from typing import Callable, Dict, Type

from d3.common.rpc.api_base import ApiBase

AnyApiBase = Type[ApiBase]
Handler = Callable[[AnyApiBase], AnyApiBase]


@dataclass()
class HandlerMeta:
    api_name: str
    constructor: Callable[[dict], object]
    handler: Handler


class RpcHandlers:
    def __init__(self):
        self.handlers_meta: Dict[str, HandlerMeta] = dict()

    def register(self, handler: Handler):
        s = inspect.signature(handler)
        params = s.parameters
        if len(params) != 1:
            raise Exception('The handler must have exactly one parameter')
        name = next(iter(params))
        param = params[name]
        request_type = param.annotation
        response_type = s.return_annotation
        self.check(request_type, f'parameter {name}')
        self.check(response_type, f'return type')
        ApiBase.check_request_completeness(request_type)
        api_name = request_type.__name__
        self.handlers_meta[api_name] = HandlerMeta(api_name=api_name, constructor=request_type, handler=handler)

    def check(self, annotation, annotation_name):
        if annotation == inspect._empty:
            raise Exception(f'You must specify the type annotation for {annotation_name}')
        if not issubclass(annotation, ApiBase) or annotation == ApiBase:
            raise Exception(f'{annotation_name} must extend class ApiBase')

    def dispatch(self, request):
        name = request.__class__.__name__
        meta = self.handlers_meta.get(name, None)
        if meta is None:
            raise Exception(f'Handler not found for `{name}`')
        return meta.handler(request)

    def dispatch_str(self, name: str, json_payload: str) -> str:
        meta = self.handlers_meta[name]
        args = json.loads(json_payload)
        request = meta.constructor(**args)
        response = meta.handler(request)
        response_json = response.json()
        return response_json
