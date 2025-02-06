from flask import Flask, Blueprint

from api import api

server = Flask(__name__)

server.register_blueprint(api)

if __name__ == '__main__':
    server.run()
