from js import console, fetch, document

from app.common.rpc.api_base import api_send_set
from app.common.rpc.rpc_send import RpcSend


async def _fetch_send(name: str, json_payload: str) -> str:
    response = await fetch(
        f'http://localhost:5020/api_handler?name={name}',
        method='POST',
        body=json_payload
    )
    json = await response.text()
    console.log(f'json response for {name}', json)
    return json


def rpc_browser_setup():
    api_send_set(RpcSend(_fetch_send).send)
