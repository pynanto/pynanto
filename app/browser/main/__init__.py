from js import document

from app.browser.rpc import rpc_browser_setup
from app.browser.widget import widget_test
from app.browser.widget_library.edit_widget import EditWidget
from app.common.api.api_product import ApiProductRequest, ApiProductResponse


async def main():
    rpc_browser_setup()

    ed1 = EditWidget('A').append_to(document.body)
    ed2 = EditWidget('B').append_to(document.body)
    ed3 = EditWidget('A*B=').append_to(document.body)

    async def run_sum():
        res: ApiProductResponse = await ApiProductRequest(a=ed1.value, b=ed2.value).send()
        ed3.value = str(res.product)

    for ed in [ed1, ed2]:
        ed.oninput = lambda x: run_sum()

    widget_test.main()
