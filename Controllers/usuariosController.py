from flask import Blueprint, jsonify
from Dtos.Usuario.usuarioDto import UserDto
from Services.UsuarioService import UsuarioService

usuariosController = Blueprint('usuariosController', __name__)
usuarioService = UsuarioService()


@usuariosController.route("/")
def getAll():
    users = usuarioService.getAll()
    usersdto = UserDto(many=True)
    result = usersdto.dump(users)
    return jsonify(result)


@usuariosController.route("/<int:id>")
def getId(id):
    user = usuarioService.getId(id)
    usersdto = UserDto()
    result = usersdto.dump(user)
    return jsonify(result)
