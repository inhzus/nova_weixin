# -*- coding: utf-8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from flask import Blueprint

bind = Blueprint('bind', __name__)
from app.bind import views
