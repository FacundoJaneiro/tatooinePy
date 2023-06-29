from flask import Blueprint, jsonify, request
from Exceptions.wrapperExceptions import handle_exceptions
from Handlers.tokensHandler import TokenHandler
from Services.ComponenteService import ComponenteService
from Dtos.Componente.Responses.componenteDto import ComponenteDto

componenteController = Blueprint('componenteController', __name__)
tokenHandler = TokenHandler()
componenteService = ComponenteService()


@componenteController.route("/materiasPrimas", methods=['GET'])
@componenteController.route("/insumos", methods=['GET'])
@handle_exceptions
def getComponentes():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    tipo = 1 if 'materiasPrimas' in request.path else 2
    componentes = componenteService.getAll(tipo)
    componenteDto = ComponenteDto(many=True)
    result = componenteDto.dump(componentes)
    return jsonify(result)


@componenteController.route("/materiasPrimas/<int:id>", methods=['GET'])
@componenteController.route("/insumos/<int:id>", methods=['GET'])
@handle_exceptions
def getId(id):
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    tipo = 1 if 'materiasPrimas' in request.path else 2
    componente = componenteService.getId(tipo,id)
    componenteDto = ComponenteDto()
    result = componenteDto.dump(componente)
    return jsonify(result)
