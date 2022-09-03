from js import document

from app.browser.pyscript_examples.d3js_demo.d3js_demo_widget import D3_DemoWidget
from app.browser.rpc import global_transport_set_url
from app.browser.use_case_01.use_case_01_widget import UseCase01Widget
from app.browser.usecase02.UseCase02_Widget import UseCase02_Widget
from app.browser.widget_forms.square_widget import SquareWidget


async def main():

    global_transport_set_url('http://localhost:5020/api_handler?name={api_name}')

    widget_instances = [
        # PanelKMeansClusteringDemoWidget(),
        # FutureWidget(),
        # D3_DemoWidget(),
        # RequestWidget(),
        # FilesystemTreeWidget(),
        # ProductWidget(),
        UseCase02_Widget(),
        D3_DemoWidget(),
        # SquareWidget(),
    ]

    [w.append_to(document.body) for w in widget_instances]

    tests()


def tests():
    from app.browser.unittest_fix import run_all_tests
    run_all_tests()
