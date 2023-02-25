from marshmallow import Schema, fields


class UserDto(Schema):
    PK_usuario = fields.Integer()
    nombreUsuario = fields.String()
    apellidoUsuario = fields.String()
    statusUsuario = fields.String()
    emailUsuario = fields.String()
    passwordUsuario = fields.String()
    avatarUsuario = fields.String()
    descripcionRol = fields.String(attribute='rol.descripcionRol')
    seguridadRol = fields.String(attribute='rol.seguridadRol')
