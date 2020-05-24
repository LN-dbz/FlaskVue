from sqlalchemy import Column, String, Integer
from .base import Base


# 用户表
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User name>'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
    def to_json_1(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }