import asyncio

from app.browser.html.dom_async import load_script
from js import console

_loaded = False
_lock = asyncio.Lock()


async def load_d3():
    global _loaded
    async with _lock:
        if _loaded:
            console.log('d3 js already loaded')
            return
        _loaded = True
        await load_script(src='https://d3js.org/d3.v7.min.js')
