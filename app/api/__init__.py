from .category_api import bp as category_bp
from .project_api import bp as project_bp
from .timelog_api import bp as timelog_bp
# from .user_api import bp as user_bp  # 如果启用用户接口

from flask_restx import Api

__all__ = ['category_bp', 'project_bp', 'timelog_bp']

api_blueprints = [category_bp, project_bp, timelog_bp]


def init_app(app):
    for bp in api_blueprints:
        app.register_blueprint(bp)