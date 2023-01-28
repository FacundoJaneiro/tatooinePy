from flask import Blueprint, jsonify, request
from Entities.usuario import User
from Dtos.Usuario.usuarioDto import UserDto
from Dtos.Usuario.userAltaDto import UserAltaDto
from Exceptions.baseException import BaseException
from Exceptions.missingDataRequiredException import MissingDataRequiredException
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


@usuariosController.route("/", methods=['POST'])
def create():
    try:
        userDto = UserAltaDto()
        errors = userDto.validate(request.json)
        if errors:
            raise MissingDataRequiredException
        data = userDto.load(request.json)
        user = User(**data)
        usuarioService.save(user)
        return jsonify({"message": "User created successfully"}), 201
    except BaseException as e:
        return jsonify({"error": e.getMessage()}), e.getCode()
    except Exception as e:
        return jsonify({"error": "An internal server error occurred"}), 500


