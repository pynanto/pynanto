from js import document

from app.browser.rpc import rpc_browser_setup
from app.browser.widget import widget_test
from app.browser.widget_forms.product_widget import ProductWidget


async def main():
    rpc_browser_setup()
    ProductWidget().append_to(document.body)
    widget_test.main()
