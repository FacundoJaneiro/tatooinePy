from flask import Blueprint, jsonify, request
from Entities.usuario import User
from Dtos.Usuario.usuarioDto import UserDto
from Dtos.Usuario.userAltaDto import UserAltaDto
from Dtos.Usuario.userModificacionDto import UserModificacionDto
from Exceptions.wrapperExceptions import handle_exceptions
from Services.UsuarioService import UsuarioService

usuariosController = Blueprint('usuariosController', __name__)
usuarioService = UsuarioService()


@usuariosController.route("/")
@handle_exceptions
def getAll():
    users = usuarioService.getAll()
    usersdto = UserDto(many=True)
    result = usersdto.dump(users)
    return jsonify(result)


@usuariosController.route("/<int:id>")
@handle_exceptions
def getId(id):
    user = usuarioService.getId(id)
    usersdto = UserDto()
    result = usersdto.dump(user)
    return jsonify(result)


@usuariosController.route("/", methods=['POST'])
@handle_exceptions
def create():
    userDto = UserAltaDto()
    data = userDto.load(request.json)
    user = User(**data)
    usuarioService.save(user)
    return jsonify({"message": "User created successfully"}), 201


@usuariosController.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id):
    usuarioService.delete(id)
    return jsonify({"message": "User deleted successfully"}), 201


@usuariosController.route("/", methods=['PUT'])
@handle_exceptions
def modify():
    dto = UserModificacionDto()
    data = dto.load(request.json)
    user = User(**data)
    usuarioService.modify(user)
    return jsonify({"message": "User modify successfully"}), 201
