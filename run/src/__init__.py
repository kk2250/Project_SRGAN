#!/usr/bin/evn python3

import os

from flask import Flask, render_template

from .controller.public import controller

omnibus = Flask(__name__)

omnibus.register_blueprint(controller)