#!/usr/bin/env python
"""MCWebViz"""

import os.path
import logging, logging.handlers
from logging.handlers import RotatingFileHandler

from flask import Flask, abort, request, send_from_directory, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = os.path.dirname('uploads/')
RENDER_FOLDER = os.path.dirname('renders/')
FILE_HANDLER = RotatingFileHandler('log/flask.log')

APP = Flask(__name__)
APP.logger.addHandler(FILE_HANDLER)
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP.config['RENDER_FOLDER'] = RENDER_FOLDER
from mcviz.logger import LOG
for handler in APP.logger.handlers:
    LOG.addHandler(handler)

from mcviz.options import parse_options
from mcviz.tools.tools import tool_classes
from mcviz.graph import EventGraph
from mcviz.workspace import GraphWorkspace
from mcviz.web.url_hash import url_hash

def get_resource_path(folder, file_name):
    """Return absolute path to file in a resource folder"""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        APP.config[folder], file_name)

@APP.route("/")
def main():
    """Site main page"""
    APP.logger.info("Hit")
    return render_template('main.html', tools=tool_classes)

@APP.route("/render", methods=['GET', 'POST'])
def render():
    """Receive a request to render an event"""
    if request.method == 'POST':
        APP.logger.info("Rendering")
        APP.logger.debug(request.files)
        if not request.files:
            APP.logger.warning("No file received")
            abort(400)
        received_file = request.files['file']
        if not received_file:
            APP.logger.warning("No file")
            abort(400)
        file_name = secure_filename(received_file.filename)
        file_hash = url_hash(received_file.__hash__())
        APP.logger.info("received: \"%s\" hash: \"%s\"", file_name, file_hash)
        APP.logger.debug(request.form)
        for option, value in request.form.iteritems(True):
            APP.logger.debug(str(option) + ":" + str(value))
        received_file.save(os.path.join(APP.config['UPLOAD_FOLDER'], file_hash))
        opt_string = "&".join(["=".join(pair)
                               for pair in request.form.iteritems(True)])
        APP.logger.debug(opt_string)
        return render_template('render.html', tools=tool_classes,
                               file_name=file_hash, opt_string=opt_string)
    else:
        abort(400)

@APP.route("/render/<name>", methods=['GET', 'POST'])
def rerender(name):
    """Receive a request to re-render an event"""
    if request.method == 'POST':
        APP.logger.info("Rendering POST")
        args = request.form
    else:
        APP.logger.info("Rendering GET")
        args = request.args
    opt_string = "&".join(["=".join(pair) for pair in args.iteritems(True)])
    APP.logger.debug(opt_string)
    return render_template('render.html', tools=tool_classes,
                           file_name=name, opt_string=opt_string)

@APP.route("/image/<file_name>")
def get_image(file_name):
    """Serve image back to user"""
    name, _, _ = file_name.rpartition(".")
    APP.logger.info("Rendering image %s", name)
    APP.logger.debug(request.args)
    arg_list = [e for pair in request.args.iteritems(True) for e in pair]
    APP.logger.debug(arg_list)
    _, args = parse_options(arg_list)
    APP.logger.debug(args)
    args.filename = get_resource_path('UPLOAD_FOLDER', name)
    args.output_file = get_resource_path('RENDER_FOLDER', file_name)

    event_graph = EventGraph.load(args)
    workspace = GraphWorkspace(name, event_graph)
    workspace.load_tools(args)
    workspace.run()

    APP.logger.info("Rendering %s done", name)
    return send_from_directory("renders/", file_name)

if __name__ == "__main__":
    from logging import Formatter
    TEMPLATE = "[%(asctime)s|%(levelname)-7s] %(message)s"

    APP.debug = True
    APP.logger.setLevel(logging.DEBUG)
    for handler in APP.logger.handlers:
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(Formatter(TEMPLATE))

    APP.run(host='0')
