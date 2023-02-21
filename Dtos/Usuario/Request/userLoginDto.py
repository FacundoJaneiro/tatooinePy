from marshmallow import Schema, fields


class UserLoginDto(Schema):
    emailUsuario = fields.String(required=True, error_messages={'required': 'El campo emailUsuario es requerido.'})
    passwordUsuario = fields.String(required=True, error_messages={'required': 'El campo passwordUsuario es requerido.'})
