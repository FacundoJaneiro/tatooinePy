from marshmallow import Schema, fields


class UserAltaDto(Schema):
    nombreUsuario = fields.String(required=True, error_messages={'required': 'El campo nombreUsuario es requerido.'})
    apellidoUsuario = fields.String(required=True, error_messages={'required': 'El campo apellidoUsuario es requerido.'})
    statusUsuario = fields.Integer(default=1)
    emailUsuario = fields.String(required=True, error_messages={'required': 'El campo emailUsuario es requerido.'})
    passwordUsuario = fields.String(required=True, error_messages={'required': 'El campo passwordUsuario es requerido.'})
    avatarUsuario = fields.String(required=True, error_messages={'required': 'El campo avatarUsuario es requerido.'})
    FK_rol = fields.Integer(required=True, error_messages={'required': 'El campo FK_rol es requerido.'})
