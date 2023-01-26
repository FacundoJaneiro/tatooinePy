from flask import Blueprint, jsonify
from Dtos.usuario import UserDto
from Entities.usuario import User

usuariosController = Blueprint('usuariosController', __name__)


@usuariosController.route("/")
def hello():
    user = User.query.filter_by(PK_usuario=1).first()
    usersdto = UserDto()
    result = usersdto.dump(user)
    return jsonify(result)
