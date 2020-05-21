from flask_restful import Resource


class ApiView(Resource):

    def get(self):
        # 这里不用再自己手动调用jsonify()了
        return {'code': 200, 'msg': 'ok'}

