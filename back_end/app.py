from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from .config import config
from .api import all_view, all_api
from .module.database import init_db

from flask import Flask, request, session
from flask_session import Session


# flask工厂函数
def create_app(run_type='default'):
    app = Flask(__name__)
    # 数据库
    # 初始化db,并创建models中定义的表格,每次初始化不会删除之前的数据
    init_db()
    app.config.from_object(config[run_type])
    # session 注册
    # f_session = Session()
    # 绑定flask的对象
    # f_session.init_app(app)
    # Session(app=app)
    # jwt 注册
    # jwt = JWT(app, authenticate, identity)
    # view 的注册
    for api_obj in all_view:
        app.register_blueprint(api_obj['api'], url_prefix=api_obj['endpoint'])
    api = Api(app)
    # api 的注册
    for api_obj in all_api:
        api.add_resource(api_obj['api'], api_obj['endpoint'])

    return app
