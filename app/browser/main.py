from js import document

from app.browser.rpc import rpc_browser_setup
from app.browser.widget import test_widget
from app.browser.widget_forms.product_widget import ProductWidget


async def main():
    rpc_browser_setup()
    ProductWidget().append_to(document.body)
    test_widget.main()
