from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return "User(id='%s')" % self.id

    def genTokenSeq(self, expires, ini):
        s = Serializer(
            secret_key=ini['SECRET_KEY'],
            salt=ini['AUTH_SALT'],
            expires_in=expires)
        timestamp = time.time()
        return s.dumps({'user_id': self.id, 'user_role': self.role, 'iat': timestamp})

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


# 密码验证
def authenticate(username, password):
    print(username)
    user = username_table.get(username)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


# 身份验证
def identity(payload):
    print(payload)
    user_id = payload['identity']
    return userid_table.get(user_id, None)