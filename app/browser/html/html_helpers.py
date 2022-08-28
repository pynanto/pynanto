from functools import partial

from js import document, window, console, setInterval, fetch

from app.browser.html.dom_definitions import HTMLElement


def _ce(tag, html=None) -> HTMLElement:
    element = document.createElement(tag)
    if html is not None:
        element.innerHTML = html
    return element


def div(): return _ce('div')


def button(): return _ce('button')


def script(): return _ce('script')


def br(): return _ce('br')


def ol(): return _ce('ol')


li = partial(_ce, 'li')
