import os

from js import document, console

from app.browser.rpc import rpc_browser_setup
from app.browser.widget_components.filesystem_tree_widget import FilesystemTreeWidget
from app.browser.widget_forms.product_widget import ProductWidget


async def main():
    getcwd = os.getcwd()
    console.log('cwd', getcwd)
    rpc_browser_setup()
    # FilesystemTreeWidget().append_to(document.body)
    # ProductWidget().append_to(document.body)
    # test_widget.main()
    from app.browser.unittest import run_all_tests
    run_all_tests()
