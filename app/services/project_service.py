from app.models.project import Project
from app.models.category import Category
from app.extension import db

class ProjectService:
    @staticmethod
    def list_all():
        return Project.query.order_by(Project.id).all()

    @staticmethod
    def create(name, category_id):
        if not (name and category_id):
            raise ValueError('name 和 category_id 为必填')
        if not Category.query.get(category_id):
            raise LookupError('分类不存在')
        proj = Project(name=name, category_id=category_id)
        db.session.add(proj)
        db.session.commit()
        return proj