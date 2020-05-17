# coding: utf-8

# Author: Madalin Popa
# Date: duminică, mai 2020

from flask import Flask


def create_app():
    """
    Appication factory.
    """
    app = Flask(__name__)

    from demo.routes.main import mainbp

    app.register_blueprint(mainbp)

    return app

