from app.server.api_handlers.rpc_registrations import rpc_handlers
from app.server.bootstrap import javascript_bootstrap_code_response, client_bundle_response, \
    bootstrap_index_html_response
from flask import Flask, Response, request


def start():
    app = Flask(__name__)

    @app.route("/")
    def index_html():
        return to_flask(bootstrap_index_html_response())

    @app.route("/pynanto_bootstrap.js")
    def bootstrap_js():
        return to_flask(javascript_bootstrap_code_response())

    @app.route("/client_bundle.zip")
    def client_bundle():
        return to_flask(client_bundle_response())

    @app.route("/api_handler", methods=['GET', 'POST'])
    def hello_world():
        name = request.args.get('name')
        data = request.data
        return rpc_handlers.dispatch_str(name, data)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        return response

    app.run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)


def to_flask(pn_response) -> Response:
    return Response(pn_response.content, pn_response.mimetype)
