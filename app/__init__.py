# -*- coding:utf-8 -*-
from flask import Flask


app = Flask(__name__)


def create_app():

    from sample import sample_blueprint
    app.register_blueprint(sample_blueprint)

    return app