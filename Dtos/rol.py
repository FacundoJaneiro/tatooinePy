from marshmallow import Schema, fields


class RolDto(Schema):
    PK_rol = fields.Integer()
    descripcionRol = fields.String()
    seguridadRol = fields.Integer()
