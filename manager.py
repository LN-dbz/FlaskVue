import os
from flask_script import Manager
from back_end.app import create_app

# 运行模式写进环境变量
run_type = os.environ.get('RUN_TYPE', 'dev')
app = create_app(run_type)
manager = Manager(app)


# 举例
@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='www.csdn.com')
def hello(name, url):
    print(f'name:{name} url:{url}')


# 运行开发环境
@manager.command
def dun_dev():
    app.run(debug=True)


# manager.add_command('dev', DevRun())

if __name__ == '__main__':
    manager.run()
