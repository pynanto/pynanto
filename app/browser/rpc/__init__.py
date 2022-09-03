from js import console, fetch

from app.common.rpc.api_base import global_transport_set, ApiTransportType
from app.common.rpc.rpc_send import RpcSend


def global_transport_set_url(url: str):
    global_transport_set(transport_from_url(url))


def transport_from_url(url: str) -> ApiTransportType:
    async def _fetch_send(api_name: str, json_payload: str) -> str:
        response = await fetch(
            url.format(api_name=api_name),
            method='POST',
            body=json_payload
        )
        json = await response.text()
        console.log(f'json response for {api_name}', json)
        return json

    return RpcSend(_fetch_send).send
