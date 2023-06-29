from marshmallow import Schema, fields


class ComponenteDto(Schema):
    PK_componente = fields.Integer()
    identifiacion = fields.String()
    nombre = fields.String()
    descripcion = fields.String()
    codigo = fields.String()
    stock = fields.Float()
    stockMinimo = fields.Float()
    stockVirtual = fields.Float()
    rubro = fields.String(attribute='rubro.nombreRubro')
    unidadMedida = fields.String(attribute='unidadMedida.nombreUnidadMedida')
    denomUnidadMedida = fields.String(attribute='unidadMedida.denominacionUnidadMedida')