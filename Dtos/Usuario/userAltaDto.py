from marshmallow import Schema, fields


class UserAltaDto(Schema):
    nombreUsuario = fields.String(required=True)
    apellidoUsuario = fields.String(required=True)
    statusUsuario = fields.Integer(default=1)
    emailUsuario = fields.String(required=True)
    passwordUsuario = fields.String(required=True)
    avatarUsuario = fields.String(required=True)
    FK_rol = fields.Integer(required=True)
