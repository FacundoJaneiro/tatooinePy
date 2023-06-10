from marshmallow import Schema, fields


class UserDto(Schema):
    PK_usuario = fields.Integer()
    nombreUsuario = fields.String()
    apellidoUsuario = fields.String()
    emailUsuario = fields.String()
    avatarUsuario = fields.String()
    descripcionRol = fields.String(attribute='rol.descripcionRol')
