from flask import Blueprint, jsonify, request
from Exceptions.wrapperExceptions import handle_exceptions
from Handlers.tokensHandler import TokenHandler
from Services.MateriaPrimaService import MateriaPrimaService
from Dtos.MateriaPrima.Responses.materiaPrimaDto import MateriaPrimaDto

materiasPrimasController = Blueprint('materiasPrimasController', __name__)
tokenHandler = TokenHandler()
materiaPrimaService = MateriaPrimaService()


@materiasPrimasController.route("/")
@handle_exceptions
def getAll():
    tokenHandler.validator(request.headers.get('Authorization'), ['Administrador'])
    materiasPrimas = materiaPrimaService.getAll()
    mpDto = MateriaPrimaDto(many=True)
    result = mpDto.dump(materiasPrimas)
    return jsonify(result)
