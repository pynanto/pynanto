# Browse pyscript virtual filesystem
import os
import sys
from pathlib import Path
from typing import List

import js
from js import console
from pyodide import create_proxy, to_js

from app.browser.html.dom_definitions import HTMLElement
from app.browser.widget.widget import Widget


class FilesystemTreeWidget(Widget):
    def __init__(self, path: Path = Path('/'), indent=1):
        self._indent = indent
        super().__init__(  # language=HTML
            f"""
            <span id="_entity"></span>
            <span id="_download">&nbsp ↓ &nbsp</span>
            <div id="_children" style="margin-left: 1em"></div>
            
            """
        )
        self.path = Path(path)
        self._entity: HTMLElement = self
        self._children: HTMLElement = self
        self._download: HTMLElement = self

    def after_render(self):

        self._entity.onclick = create_proxy(self.toggle_display)
        self._download.onclick = create_proxy(self.download)
        if self._indent > 1:
            self.toggle_display()

        self._update_caption()

        if self.is_dir():
            self._recurse()

    def is_dir(self):
        # return self.path.is_dir() # in pyodide: `PermissionError: [Errno 63] Operation not permitted: '/proc/self/fd'`
        return os.path.isdir(self.path)

    def toggle_display(self, *args):
        self._children.style.display = '' if self._children_hidden() else 'none'
        self._update_caption()

    def download(self, *args):
        console.log(f'click {self.path.absolute()}')

    def _update_caption(self):
        if_dir = '▸' if self._children_hidden() else '▼'
        pre = if_dir if self.is_dir() else ' '
        self._entity.innerHTML = (f'<span style="display:inline-block; width: 1em">{pre}</span>'
                                  + ' ' + self.path.name)

    def _children_hidden(self):
        s = self._children.style
        return not s.display == ''

    def _recurse(self):
        for child in self.path.glob('*'):
            w = FilesystemTreeWidget(child, self._indent + 1)
            w.append_to(self._children)
