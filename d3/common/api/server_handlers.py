import inspect
from typing import Callable

from pydantic import BaseModel

from d3.common.api.api_base import ApiBase


class ServerHandlers:
    def __init__(self):
        pass

    def register(self, handler: Callable[[ApiBase], ApiBase]):
        s = inspect.signature(handler)
        params = s.parameters
        if len(params) != 1:
            raise Exception('The handler must have exactly one parameter')
        name = next(iter(params))
        param = params[name]
        self.check(param.annotation, f'parameter {name}')
        self.check(s.return_annotation, f'return type')

        pass

    def check(self, annotation, annotation_name):
        if annotation == inspect._empty:
            raise Exception(f'You must specify the type annotation for {annotation_name}')
        if not issubclass(annotation, ApiBase) or annotation == ApiBase:
            raise Exception(f'{annotation_name} must extend class ApiBase')
