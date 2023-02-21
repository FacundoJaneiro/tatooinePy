from marshmallow import Schema, fields


class UserModificacionDto(Schema):
    PK_usuario = fields.Integer(required=True, error_messages={'required': 'El campo PK_usuario es requerido.'})
    nombreUsuario = fields.String()
    apellidoUsuario = fields.String()
    emailUsuario = fields.String()
    avatarUsuario = fields.String()
    FK_rol = fields.Integer()
