from js import document

from app.browser.pyscript_examples.panel_kmeans.panel_kmeans_clustering_demo import PanelKMeansClusteringDemoWidget
from app.browser.rpc import rpc_browser_setup


async def main():

    rpc_browser_setup()

    widget_instances = [
        PanelKMeansClusteringDemoWidget(),
        # FilesystemTreeWidget(),
        # ProductWidget(),
        # SquareWidget(),
        # SquareWidget(),
    ]

    [w.append_to(document.body) for w in widget_instances]

    tests()


def tests():
    from app.browser.unittest_fix import run_all_tests
    run_all_tests()
