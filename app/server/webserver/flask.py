from pathlib import Path

from flask import Flask, Response, request, send_file

from app.server.api_handlers.rpc_registrations import rpc_handlers
from app.common.sources.client_bundle import build_archive

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response


@app.route("/api_handler", methods=['GET', 'POST'])
def hello_world():
    name = request.args.get('name')
    data = request.data
    return rpc_handlers.dispatch_str(name, data)


@app.route("/client_bundle.zip")
def client_bundle():
    print('serving client_bundle.zip with content-type')
    return Response(build_archive(),
                    mimetype='application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip')


@app.route("/")
def index_html():
    return send_file('../../browser/index.html')


@app.route("/pynanto_bootstrap.js")
def bootstrap_js():
    return Response((Path(__file__).parent / '../bootstrap/pynanto_bootstrap.js').read_text(),
                    mimetype='text/javascript')


def start():
    app.run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)
