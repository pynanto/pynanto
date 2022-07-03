# Browse pyscript virtual filesystem
import os
import sys
from pathlib import Path
from typing import List

import js
from pyodide import create_proxy, to_js

from app.browser.html.dom_definitions import HTMLElement
from app.browser.widget.widget import Widget


class FilesystemTreeWidget(Widget):
    def __init__(self, start_dir: Path = Path('/'), indent=1):
        self._indent = indent
        super().__init__(  # language=HTML
            f"""
            <span id="_entity"></span><span> ↓ </span>
            <div id="_children" style="margin-left: 1em"></div>
            
            """
        )
        self.start_dir = Path(start_dir)
        self._entity: HTMLElement = self
        self._children: HTMLElement = self

    def after_render(self):

        self._entity.onclick = create_proxy(self.toggle_display)
        if self._indent > 1:
            self.toggle_display()

        self._update_caption()

        if os.path.isdir(self.start_dir):
            self._recurse()

    def toggle_display(self, *args):
        self._children.style.display = '' if self._children_hidden() else 'none'
        self._update_caption()

    def _update_caption(self):
        def w(text): return f'<span style="display:inline-block; width: 1em">{text}</span>'

        pre = w('▸') if self._children_hidden() else w('▼')
        self._entity.innerHTML = pre + ' ' + self.start_dir.name

    def _children_hidden(self):
        s = self._children.style
        return not s.display == ''

    def _recurse(self):
        for child in self.start_dir.glob('*'):
            w = FilesystemTreeWidget(child, self._indent + 1)
            w.append_to(self._children)
