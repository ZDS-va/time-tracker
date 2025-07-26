from app.models.category import Category
from app.extension import db

class CategoryService:
    @staticmethod
    def list_all():
        return Category.query.order_by(Category.id).all()

    @staticmethod
    def create(name):
        if not name:
            raise ValueError('分类名不能为空')
        if Category.query.filter_by(name=name).first():
            raise ValueError('分类已存在')
        cat = Category(name=name)
        db.session.add(cat)
        db.session.commit()
        return cat