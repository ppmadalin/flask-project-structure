# coding: utf-8

# Author: Madalin Popa
# Date: duminică, mai 2020

from demo import flask_app

app = flask_app.create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
