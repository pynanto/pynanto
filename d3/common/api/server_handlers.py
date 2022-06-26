import inspect
from typing import Callable, Dict, TypeVar, Type

from pydantic import BaseModel

from d3.common.api.api_base import ApiBase

# AnyApiBase = TypeVar('AnyApiBase', bound=ApiBase, contravariant=True)
AnyApiBase = Type[ApiBase]
Handler = Callable[[AnyApiBase], AnyApiBase]


class ServerHandlers:
    def __init__(self):
        self.handlers: Dict[str, Handler] = dict()

    def register(self, handler: Handler):
        s = inspect.signature(handler)
        params = s.parameters
        if len(params) != 1:
            raise Exception('The handler must have exactly one parameter')
        name = next(iter(params))
        param = params[name]
        self.check(param.annotation, f'parameter {name}')
        self.check(s.return_annotation, f'return type')
        api_name = param.annotation.__name__
        self.handlers[api_name] = handler

    def check(self, annotation, annotation_name):
        if annotation == inspect._empty:
            raise Exception(f'You must specify the type annotation for {annotation_name}')
        if not issubclass(annotation, ApiBase) or annotation == ApiBase:
            raise Exception(f'{annotation_name} must extend class ApiBase')

    def dispatch(self, request):
        name = request.__class__.__name__
        handler = self.handlers.get(name, None)
        if handler is None:
            raise Exception(f'Handler not found for `{name}`')
        return handler(request)
