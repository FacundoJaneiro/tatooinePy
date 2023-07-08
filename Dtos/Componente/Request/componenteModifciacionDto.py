from marshmallow import Schema, fields


class ComponenteModificacionDto(Schema):
    PK_componente = fields.Integer(required=True, error_messages={'required': 'El campo PK_componente es requerido.'})
    identificacion = fields.String()
    nombre = fields.String()
    descripcion = fields.String()
    codigo = fields.String()
    stock = fields.Decimal()
    stockMinimo = fields.Decimal()
    stockVirtual = fields.Decimal()
    FK_rubro = fields.Integer()
    FK_unidadMedida = fields.Integer()
