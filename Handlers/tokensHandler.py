import os

import jwt

from Exceptions.InvalidTokenException import InvalidTokenException


class TokenHandler:
    def __init__(self):
        self.secret_key = os.environ.get('SECRET_KEY')

    def encode_token(self, payload):
        encoded_token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return encoded_token

    def decode_token(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return decoded_token
        
        except:
            raise InvalidTokenException
