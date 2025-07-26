from flask import Flask
from .config import Config
from .extension import db, cors
from .api import init_app as init_api
# from .api.user_api import bp as user_bp  # 若启用认证

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    cors.init_app(app)

    # 注册api
    init_api(app)

    return app