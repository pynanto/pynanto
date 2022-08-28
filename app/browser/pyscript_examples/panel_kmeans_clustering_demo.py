from app.browser.html.dom_definitions import HTMLElement
from app.browser.html.html_helpers import script
from app.browser.widget.widget import Widget
from js import document, console
import js
from pyodide import create_proxy


class PanelKMeansClusteringDemoWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <div>PanelKMeansClusteringDemoWidget</div>
            <button id='_btn1'>load demo</button>
        """)
        self._btn1: HTMLElement = self

    def after_render(self):
        self.container.id = "x-my-PanelKMeansClusteringDemoWidget"
        scripts = []
        for c in self.container.children:
            if c.tagName == 'SCRIPT':
                c.remove()
                scripts.append(c)
        scripts.reverse()

        def load_next(*args):
            console.log(f'load scripts len left:  {len(scripts)}')
            if len(scripts) == 0:
                console.log('load scripts done')
                return
            c = scripts.pop()
            console.log(f'script=`{c.innerHTML}`')
            s = script()
            s.type = s.type
            s.src = c.src
            # js.eval(c.innerHTML)
            if s.src == '':
                load_next()
            else:
                s.onload = create_proxy(load_next)
            document.body.append(s)

        load_next()

        self._btn1.onclick = create_proxy(self.btn1_click)

    async def btn1_click(self, *args):
        self._btn1.disabled = True
        console.log('after_append()')
        import micropip
        await micropip.install(['altair', 'numpy', 'pandas', 'scikit-learn', 'panel==0.13.1'])
        import app.browser.pyscript_examples.pyscript_example
