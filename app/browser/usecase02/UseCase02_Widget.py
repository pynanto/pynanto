from app.browser.d3helpers.d3_load import load_d3
from app.browser.html.dom_async import run_async
from app.browser.widget.widget import Widget


class UseCase02_Widget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <h2>UseCase02_Widget</h2>
            """
        )

    def after_render(self):
        run_async(self.after_render_async2())

    async def after_render_async2(self):
        await load_d3()
