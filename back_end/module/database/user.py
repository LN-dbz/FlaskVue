from sqlalchemy import Column, String, Integer
from .base import Base
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time


# 用户表
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(120))
    role = Column(String(120))

    def __init__(self, name=None, password=None, role=None):
        self.name = name
        self.role = role
        self.password = password

    def __repr__(self):
        return f'<User name>'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'role': self.role,
        }

    def tokenAuth(self, token, ini={}):
        # token decoding
        s = Serializer(
            secret_key=ini.get('SECRET_KEY', 'SECRET_KEY'),
            salt=ini.get('AUTH_SALT', 'HS256'))
        try:
            data = s.loads(token)
            return data
        except:
            return {}
    def genTokenSeq(self, expires=60*60, ini={}):
        user_information = self.auth_password()
        if user_information['code'] != 0:
            return user_information
        s = Serializer(
            secret_key=ini.get('SECRET_KEY', 'SECRET_KEY'),
            salt=ini.get('AUTH_SALT', 'HS256'),
            expires_in=1)
        timestamp = time.time()
        return s.dumps({'user_id': self.id, 'user_role': self.role, 'iat': timestamp})

    # 密码验证
    def auth_password(self):
        user = User.query.filter(User.name == self.name).all()
        if user and len(user) == 1 and self.password == user[0].to_json()['password']:
            return {'code': 0, 'data': user[0].to_json()}
        elif user:
            return {'code': 1, 'message': '密码错误！'}
        else:
            return {'code': 2, 'message': '用户名错误！'}
