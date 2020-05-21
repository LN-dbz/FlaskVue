from flask import Flask
from flask_restful import Api
from .config import config
from .api import all_api


# flask工厂函数
def create_app(run_type='default'):
    app = Flask(__name__)
    api = Api(app)
    # api 的注册
    for api_obj in all_api:
        api.add_resource(api_obj['api'], api_obj['endpoint'])
    app.config.from_object(config[run_type])

    return app