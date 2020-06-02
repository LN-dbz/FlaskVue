from flask import redirect, request, jsonify, Blueprint, session
from back_end.module.database.user import User


main = Blueprint('main', __name__)


@main.route('login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.values.get("username")
        password = request.values.get("password")

        user = User(username, password)
        result = user.auth_password()
        if result['code'] == 0:
            session['user_id'] = result['data']['id']
            return redirect('/')
        else:
            return result
    else:
        return 'login'


@main.route('/')
def index():
    return 'index'
