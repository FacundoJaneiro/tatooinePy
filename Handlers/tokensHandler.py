import datetime
import os
import jwt
from Exceptions.InvalidTokenException import InvalidTokenException
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from Exceptions.tokenNotFoundException import TokenNotFoundException
from Exceptions.unauthorizedException import UnauthorizedException


class TokenHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):

        if hasattr(self, 'initialized'):
            return

        self.initialized = True
        """"
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        self.secret_key = pem
        """
        self.public_key = os.environ.get('PUBLIC_KEY')

    def encode_token(self, payload):
        ##encoded_token = jwt.encode(payload, self.secret_key, algorithm='RS256')
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        payload['exp'] = int(exp_time.timestamp())
        encoded_token = jwt.encode(payload, self.public_key, algorithm='HS256')
        return encoded_token

    def decode_token(self, token):
        try:
            ##decoded_token = jwt.decode(token, self.public_key, algorithms=['RS256'])
            decoded_token = jwt.decode(token, self.public_key, algorithms=['HS256'])
            return decoded_token
        except:
            raise InvalidTokenException

    def validator(self, bearerToken, roles):
        if not bearerToken:
            raise TokenNotFoundException
        token = bearerToken.split(" ")[1]
        info = self.decode_token(token)

        if info["rol"] not in roles:
            raise UnauthorizedException
        return info
