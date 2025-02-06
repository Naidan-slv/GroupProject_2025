from flask import Blueprint

from controllers.user import user_controller

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(user_controller)
