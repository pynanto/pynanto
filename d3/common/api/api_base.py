from collections.abc import Callable

from pydantic import BaseModel


async def _no_send(request):
    raise Exception('no send was configured')


# api_send: Callable[['ApiBase', BaseModel]] = _no_send
api_send = _no_send


def api_send_set(send):
    global api_send
    api_send = send


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
