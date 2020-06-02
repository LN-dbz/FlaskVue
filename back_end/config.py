import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qwertyuio12345678'  # 加密的密钥
    # SESSION_USE_SIGNER = True  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_TYPE = 'null'  # session类型为redis
    # SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    PERMANENT_SESSION_LIFETIME = 7200  # 失效时间 秒
    # SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', db=4)  # redi
    JSON_AS_ASCII = False
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    pass


class DevelopmentConfig(BaseConfig):  # 开发配置
    DEBUG = True


class TestingConfig(BaseConfig):  # 测试配置
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite'))
    WTF_CSRF_ENABLED = False


config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
