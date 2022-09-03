from app.browser.d3helpers.d3_load import load_d3
from app.browser.html.dom_async import run_async, load_script
from app.browser.widget.widget import Widget
from js import console


class D3_DemoWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
         <div>
          <h2>D3_DemoWidget</h2>
          <div id="py">
            <div class="loading"></div>
          </div>
        </div>
        """
        )

    def after_render(self):
        async def doit():
            await load_d3()
            console.log('pre import')
            import app.browser.pyscript_examples.d3js_demo.app_d3 as ex
            console.log(ex.__name__)

        run_async(doit())



