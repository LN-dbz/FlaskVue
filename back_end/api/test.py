from flask_restful import Resource
from flask import Flask, request, jsonify, Blueprint

from ..module.authority.permission import permission_required
class ApiView(Resource):
    def get(self):
        # 这里不用再自己手动调用jsonify()了
        return {'code': 200, 'msg': 'ok'}


test = Blueprint('test', __name__)


@test.route('one')
@permission_required({'asd':'adasd'})
def one():
    return 'ok'

