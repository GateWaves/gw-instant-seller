import logging
import json

from flask import Flask, request
from waitress import serve

import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to GateWaves!"

@app.route("/v1/list_supported_assets")
def list_supported_assets():
    return json.dumps(config.SUPPORTED_ASSETS)

def start():
    logging.info("Starting listening on port %d" % config.PORT)
    if config.DEBUG:
        app.run(host='0.0.0.0', port=config.PORT, debug=True)
    else:
        # Do not change the number of threads.
        # The security depends on there being only one thread.
        serve(app, host='127.0.0.1', port=config.PORT, threads=1)
