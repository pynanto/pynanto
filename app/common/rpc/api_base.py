from typing import Callable, Coroutine, Awaitable

from pydantic import BaseModel


class ApiBase(BaseModel):
    class Config:
        validate_assignment = True

    async def send(self):
        return await api_send(self)

    @classmethod
    def check_request_completeness(cls, request_type):
        if not hasattr(request_type, 'response_type'):
            name = request_type.__name__
            raise Exception(f'Request type `{name}` must have a static '
                            f'property `response_type` to designate the response type')


async def _no_send(request):
    raise Exception('no send was configured. Use `api_send_set(...)`.')


ApiSendType = Callable[[ApiBase], Awaitable[BaseModel]]
api_send: ApiSendType = _no_send


def api_send_set(send: ApiSendType):
    global api_send
    api_send = send
