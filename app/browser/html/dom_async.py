import asyncio

from js import document, console
from pyodide.ffi import create_proxy
import js


async def load_script(src: str):
    f = asyncio.Future()
    s = document.createElement('script')
    s.src = src
    s.onload = create_proxy(lambda x: f.set_result('ok'))
    document.body.append(s)
    res = await f
    console.log('await is', res)


def run_async(*args):
    asyncio.get_event_loop().run_until_complete(*args)
