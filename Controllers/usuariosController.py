from flask import Blueprint, jsonify, request
from Entities.usuario import User
from Dtos.Usuario.Responses.usuarioDto import UserDto
from Dtos.Usuario.Request.userAltaDto import UserAltaDto
from Dtos.Usuario.Request.userModificacionDto import UserModificacionDto
from Dtos.Usuario.Request.userLoginDto import UserLoginDto
from Exceptions.wrapperExceptions import handle_exceptions
from Handlers.tokensHandler import TokenHandler
from Services.UsuarioService import UsuarioService

usuariosController = Blueprint('usuariosController', __name__)
tokenHandler = TokenHandler()
usuarioService = UsuarioService()


@usuariosController.route("/")
@handle_exceptions
def getAll():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    users = usuarioService.getAll()
    usersdto = UserDto(many=True)
    result = usersdto.dump(users)
    return jsonify(result)


@usuariosController.route("/<int:id>")
@handle_exceptions
def getId(id):
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    user = usuarioService.getId(id)
    usersdto = UserDto()
    result = usersdto.dump(user)
    return jsonify(result)


@usuariosController.route("/", methods=['POST'])
@handle_exceptions
def create():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    userDto = UserAltaDto()
    data = userDto.load(request.json)
    user = User(**data)
    usuarioService.save(user)
    return jsonify({"message": "User created successfully"}), 201


@usuariosController.route("/<int:id>", methods=['DELETE'])
@handle_exceptions
def delete(id):
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    usuarioService.delete(id)
    return jsonify({"message": "User deleted successfully"}), 204


@usuariosController.route("/", methods=['PUT'])
@handle_exceptions
def modify():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    dto = UserModificacionDto()
    data = dto.load(request.json)
    user = User(**data)
    usuarioService.modify(user)
    return jsonify({"message": "User modify successfully"}), 200


@usuariosController.route("/login", methods=['POST'])
@handle_exceptions
def login():
    dto = UserLoginDto()
    data = dto.load(request.json)
    user = User(**data)
    info = usuarioService.login(user)
    token = tokenHandler.encode_token(info)
    return jsonify({"token": token}), 200
