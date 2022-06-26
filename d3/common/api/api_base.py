from pydantic import BaseModel


async def _no_send(request):
    raise Exception('no send was configured')


api_send = _no_send


def api_send_set(send):
    global api_send
    api_send = send


class ApiBase(BaseModel):
    class Config:
        validate_assignment = True

    async def send(self):
        return await api_send(self)


