# -*- coding:utf-8 -*-
from flask import render_template

from . import sample_blueprint


@sample_blueprint.route('/')
def index():
    return render_template('sample/index.html')