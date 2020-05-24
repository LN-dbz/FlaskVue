from flask import Flask
from flask_restful import Api
from .config import config
from .api import all_view, all_api
from .module.database import init_db


# flask工厂函数
def create_app(run_type='default'):
    app = Flask(__name__)
    api = Api(app)
    # view 的注册
    for api_obj in all_view:
        app.register_blueprint(api_obj['api'], url_prefix=api_obj['endpoint'])
    # api 的注册
    for api_obj in all_api:
        api.add_resource(api_obj['api'], api_obj['endpoint'])
    # 数据库
    # 初始化db,并创建models中定义的表格,每次初始化不会删除之前的数据
    init_db()
    app.config.from_object(config[run_type])

    return app