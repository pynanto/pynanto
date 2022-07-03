import os

from js import document, console

from app.browser.rpc import rpc_browser_setup
from app.browser.widget_components.filesystem_tree_widget import FilesystemTreeWidget
from app.browser.widget_forms.product_widget import ProductWidget


async def main():
    getcwd = os.getcwd()
    rpc_browser_setup()
    FilesystemTreeWidget().append_to(document.body)
    ProductWidget().append_to(document.body)

    tests()


def tests():
    from app.browser.unittest_fix import run_all_tests
    run_all_tests()
