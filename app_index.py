# Browse pyscript virtual filesystem

import os
import sys
from pathlib import Path

import js
from js import document, console, setInterval
from pyodide import create_proxy

console.log('=' * 40)


def create_element(tag, innerHTML=None, parent=None):
    e = document.createElement(tag)
    if innerHTML is not None:
        e.innerHTML = innerHTML
    if parent is not None:
        parent.append(e)
    return e


def filesystem_entity(name: str, indent=1):
    container = create_element('div')
    span = create_element('span', name, parent=container)
    children = []
    if os.path.isdir(name):
        for f in os.listdir(name):
            child = ('' if name == '/' else name) + '/' + f
            child_entity = filesystem_entity(child, indent + 1)
            children.append(child_entity)

    if len(children) > 0:
        console.log('ch', name, len(children))
        children_div = create_element('div', parent=container)
        children_div.style.marginLeft = f'{indent}em'

        def toggle_display(*args):
            s = children_div.style
            s.display = 'none' if s.display == '' else ''

        span.onclick = create_proxy(toggle_display)
        if indent > 1:
            span.innerHTML += ' (+)'
            toggle_display()
        for c in children:
            children_div.append(c)
    return container


folder = (Path().home() / "additional").absolute()
sys.path.insert(0, str(folder))
print('sys.path', sys.path)

folder.mkdir(parents=True, exist_ok=True)
foo = folder / "foo.py"
foo.write_text("print('I am foo2')")

import foo

document.body.append(filesystem_entity('/'))
