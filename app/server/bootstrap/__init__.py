from pathlib import Path
from typing import Union

from app.server.bootstrap.client_bundle import build_archive


class Response:
    def __init__(self, content: Union[str, bytes], mimetype: str):
        self.content = content
        self.mimetype = mimetype


def javascript_bootstrap_code() -> str:
    return (Path(__file__).parent / 'pynanto_bootstrap.js').read_text()


def javascript_bootstrap_code_response() -> Response:
    return Response(javascript_bootstrap_code(), 'text/javascript')


def client_bundle_bytes() -> bytes:
    return build_archive()


def client_bundle_response() -> Response:
    mimetype = 'application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip'
    return Response(build_archive(), mimetype)


def bootstrap_index_html_response() -> Response:
    content = (Path(__file__).parent / 'index.html').read_text()
    return Response(content, 'plain/html')
