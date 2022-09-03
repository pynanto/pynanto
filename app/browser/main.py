from js import document

from app.browser.rpc import global_transport_set_url
from app.browser.widget_forms.product_widget import ProductWidget
from app.browser.widget_forms.square_widget import SquareWidget


async def main():

    global_transport_set_url('http://localhost:5020/api_handler?name={api_name}')

    widget_instances = [
        # PanelKMeansClusteringDemoWidget(),
        # FutureWidget(),
        # D3_DemoWidget(),
        # RequestWidget(),
        # FilesystemTreeWidget(),
        ProductWidget(),
        SquareWidget(),
        # SquareWidget(),
    ]

    [w.append_to(document.body) for w in widget_instances]

    tests()


def tests():
    from app.browser.unittest_fix import run_all_tests
    run_all_tests()
