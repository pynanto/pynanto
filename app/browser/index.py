import os
import asyncio

from js import document, window, console, setInterval, fetch
from pyodide import create_proxy, to_js
from pyodide.http import pyfetch


async def main2():
    response = await pyfetch('https://starter.simone.pro/api1?api_name=ApiAcLoginRequest')


async def main():
    response = await fetch(
        'http://localhost:5020/api_handler?name=ApiProductRequest',
        method='POST',
        body='{"a": 21 , "b": 2 }'
    )
    json = await response.text()
    console.log('json of ApiProductRequest', json)
    return json


console.log('=' * 40)
