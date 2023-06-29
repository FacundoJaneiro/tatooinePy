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
    tipo = 1 if request.path == '/componentes/materiasPrimas' else 2
    componentes = componenteService.getAll(tipo)
    componenteDto = ComponenteDto(many=True)
    result = componenteDto.dump(componentes)
    return jsonify(result)



