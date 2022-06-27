from pathlib import Path

from flask import Flask, request, send_file

from d3.server.api_server import rpc_handlers
from d3.server.client_bundle import build_archive

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
    path = build_archive()
    print('serving', path)
    return path.read_bytes()


@app.route("/")
def index_html():
    return send_file('../browser_bootstrap/index.html')


app.run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)
