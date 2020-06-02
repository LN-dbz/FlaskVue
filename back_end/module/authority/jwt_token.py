
# serializer for JWT
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time


"""
token is generated as the JWT protocol.
JSON Web Tokens(JWT) are an open, industry standard RFC 7519 method
"""


def genTokenSeq(self, expires, ini):
    s = Serializer(
        secret_key=ini['SECRET_KEY'],
        salt=ini['AUTH_SALT'],
        expires_in=expires)
    timestamp = time.time()
    return s.dumps(
        {'user_id': self.user_id,
         'user_role': self.role_id,
         'iat': timestamp})