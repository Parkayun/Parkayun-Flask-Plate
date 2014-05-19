# -*- coding:utf-8 -*-
from flask import Blueprint

sample_blueprint = Blueprint('sample', __name__)

from . import views