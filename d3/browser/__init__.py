from js import console, fetch

from d3.common.api.api_product import ApiProductRequest, ApiProductResponse
from d3.common.rpc.api_base import api_send_set
from d3.common.rpc.rpc_send import RpcSend

print('=' * 10 + ' d3.browser module initialized')


async def main():
    print('=' * 10 + ' d3.browser main')
    api_send_set(RpcSend(fetch_send).send)
    req = ApiProductRequest(a=21, b=2)
    res: ApiProductResponse = await req.send()
    print('req', req)
    print('res', res)


async def fetch_send(name: str, json_payload: str) -> str:
    response = await fetch(
        f'http://localhost:5020/api_handler?name={name}',
        method='POST',
        body=json_payload
    )
    json = await response.text()
    console.log(f'json response for {name}', json)
    return json
