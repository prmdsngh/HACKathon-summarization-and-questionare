from flask import Flask
from controller import routes
import sys

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.secret_key = 'super_secret_key'
    app.debug = False
    return app

def run_app(app):
    app.run(host='localhost', port=8001)

if __name__ == '__main__':
    app = create_app()
    routes(app)
    run_app(app)


