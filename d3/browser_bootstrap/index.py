import os
import asyncio
from pathlib import Path

from js import document, window, console, setInterval, fetch
from pyodide import create_proxy, to_js
from pyodide.http import pyfetch
import pyodide


async def main2():
    response = await pyfetch('https://starter.simone.pro/api1?api_name=ApiAcLoginRequest')


async def main():
    response = await pyfetch('http://localhost:5020/client_bundle.zip')
    await response.unpack_archive()
    import sys
    sys.path.insert(0, str(Path('./additional').absolute()))
    import d3.browser

console.log('=' * 40)
