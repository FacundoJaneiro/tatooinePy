from marshmallow import Schema, fields


class ComponenteAltaDto(Schema):
    identifiacion = fields.String(required=True, error_messages={'required': 'El campo identifiacion es requerido.'})
    nombre = fields.String(required=True, error_messages={'required': 'El campo nombre es requerido.'})
    descripcion = fields.String(required=True, error_messages={'required': 'El campo descripcion es requerido.'})
    codigo = fields.String(required=True, error_messages={'required': 'El campo codigo es requerido.'})
    stock = fields.Decimal(required=True, error_messages={'required': 'El campo stock es requerido.'})
    stockMinimo = fields.Decimal(required=True, error_messages={'required': 'El campo stockMinimo es requerido.'})
    stockVirtual = fields.Decimal(required=True, error_messages={'required': 'El campo stockVirtual es requerido.'})
    FK_rubro = fields.Integer(required=True, error_messages={'required': 'El campo FK_rubro es requerido.'})
    FK_unidadMedida = fields.Integer(required=True, error_messages={'required': 'El campo FK_unidadMedida es requerido.'})
    status = fields.Integer(default=1, missing=1)

