from .base import Base, engine

def init_db():
    """
    初始化数据文件
    :return:
    """
    from .user import User
    Base.metadata.create_all(bind=engine)
