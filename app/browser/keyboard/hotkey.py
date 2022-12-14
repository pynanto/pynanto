from typing import Callable, Optional, Dict
from pyodide.ffi import create_proxy, to_js
from js import console, window

from app.browser.html.dom_definitions import EventTarget

KeyboardEvent = object
_HotkeyHandler = Callable[[KeyboardEvent], Optional[bool]]


class Hotkey:
    def __init__(self, element: EventTarget):
        self.handlers: Dict[str, _HotkeyHandler] = dict()
        self.enable_log = False
        element.addEventListener('keydown', create_proxy(self._detect_hotkey), False)

    def add(self, hotkey: str, handler: _HotkeyHandler):
        self.handlers[hotkey] = handler

    def _detect_hotkey(self, e):
        key = ''
        if e.ctrlKey: key += 'CTRL-'
        if e.shiftKey: key += 'SHIFT-'
        if e.altKey: key += 'ALT-'
        if e.metaKey: key += 'META-'

        upc: str = e.key
        if len(upc) == 1: upc = upc.upper()

        key += upc
        if self.enable_log: console.log(key)
        handle = self.handlers.get(key, None)
        if handle is None:
            return

        res = handle(e)
        if not res:
            return

        console.log(f'prevent default for {key}')
        e.preventDefault()
        e.stopPropagation()


HotkeyWindow = Hotkey(window)
