from flask import Blueprint, jsonify, request
from Exceptions.wrapperExceptions import handle_exceptions
from Handlers.tokensHandler import TokenHandler
from Services.ComponenteService import ComponenteService
from Entities.componente import Componente
from Dtos.Componente.Responses.componenteDto import ComponenteDto
from Dtos.Componente.Request.componenteAltaDto import ComponenteAltaDto
from Dtos.Componente.Request.componenteModifciacionDto import ComponenteModificacionDto

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


@componenteController.route("/materiasPrimas",  methods=['POST'])
@componenteController.route("/insumos", methods=['POST'])
@handle_exceptions
def create():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    tipo = 1 if 'materiasPrimas' in request.path else 2
    componenteDto = ComponenteAltaDto()
    data = componenteDto.load(request.json)
    componente = Componente(**data)
    componente.tipo = tipo
    componenteService.save(componente)
    return jsonify({"message": "Componente created successfully"}), 201


@componenteController.route("/materiasPrimas", methods=['PUT'])
@componenteController.route("/insumos", methods=['PUT'])
@handle_exceptions
def modify():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    tipo = 1 if 'materiasPrimas' in request.path else 2
    dto = ComponenteModificacionDto()
    data = dto.load(request.json)
    componente = Componente(**data)
    componente.tipo = tipo
    componenteService.modify(componente)
    return jsonify({"message": "Componente modify successfully"}), 200
