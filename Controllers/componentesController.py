from flask import Blueprint, jsonify, request
from Exceptions.wrapperExceptions import handle_exceptions
from Handlers.tokensHandler import TokenHandler
from Services.ComponenteService import ComponenteService
from Dtos.Componente.Responses.componenteDto import ComponenteDto

componenteController = Blueprint('componenteController', __name__)
tokenHandler = TokenHandler()
componenteService = ComponenteService()


@componenteController.route("/<int:id>")
@handle_exceptions
def getAll(id):
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    componentes = componenteService.getAll(id)
    componenteDto = ComponenteDto(many=True)
    result = componenteDto.dump(componentes)
    return jsonify(result)



