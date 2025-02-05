from flask import Flask, Blueprint

server = Flask(__name__)
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/hello')
def hello_world():
    return 'Hello World!'

server.register_blueprint(api)

if __name__ == '__main__':
    server.run()
