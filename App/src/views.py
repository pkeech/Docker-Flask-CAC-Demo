## IMPORT REQUIRED PYTHON MODULES
#import json, uuid

## IMPORT REQUIRED FLASK MODULES
from flask import request, jsonify, make_response, current_app, render_template

## IMPORT REQUIRED CUSTOM MODULES
from src import app

## Test Index Route
@app.route("/")
def index():
    ## LOAD HEADERS
    HEADERS = request.headers['X-Dn']

    ## RETURN HELLO WORLD
    return f"<h1>Hello World!</h1><p>User DN: { HEADERS }"