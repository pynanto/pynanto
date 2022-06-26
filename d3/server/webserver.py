from flask import Flask, request

from d3.server.api_server import rpc_handlers

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


app.run(host="0.0.0.0", port=5020, debug=False, use_reloader=True)
