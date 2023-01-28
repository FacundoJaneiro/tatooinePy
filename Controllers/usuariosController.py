from flask import Blueprint, jsonify
from Dtos.Usuario.usuarioDto import UserDto
from Exceptions.baseException import BaseException
from Services.UsuarioService import UsuarioService

usuariosController = Blueprint('usuariosController', __name__)
usuarioService = UsuarioService()


@usuariosController.route("/")
def getAll():
    try:
        users = usuarioService.getAll()
        usersdto = UserDto(many=True)
        result = usersdto.dump(users)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "An internal server error occurred"}), 500


@usuariosController.route("/<int:id>")
def getId(id):
    try:
        user = usuarioService.getId(id)
        usersdto = UserDto()
        result = usersdto.dump(user)
        return jsonify(result)
    except BaseException as e:
        return jsonify({"error": e.getMessage()}), e.getCode()
    except Exception as e:
        return jsonify({"error": "An internal server error occurred"}), 500


