from js import console, fetch, document

from app.browser.rpc import rpc_browser_setup
from app.browser.widget.widget import Widget
from app.common.api.api_product import ApiProductRequest, ApiProductResponse
from app.common.rpc.api_base import api_send_set
from app.common.rpc.rpc_send import RpcSend

print('=' * 10 + ' d3.browser module initialized')


async def main():
    print('=' * 10 + ' d3.browser main')
    rpc_browser_setup()
    req = ApiProductRequest(a=21, b=2)
    res: ApiProductResponse = await req.send()
    print('req', req)
    print('res', res)
    Widget(  # language=HTML
        f"""
        <span>first widget!</span>
        <div>{res}</div>
            """
    ).append_to(document.body)
    import app.browser.d3play.app_d3


