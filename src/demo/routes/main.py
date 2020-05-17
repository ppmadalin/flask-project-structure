# coding: utf-8

# Author: Madalin Popa
# Date: duminică, mai 2020

from flask import Blueprint

mainbp = Blueprint("mainbp", __name__)


@mainbp.route("/", methods=["GET"])
def hello():
    return "Hello World!"
