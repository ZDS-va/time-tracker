# from app.models.user import User
# from app.extension import db
#
# class UserService:
#     @staticmethod
#     def get_by_username(username):
#         return User.query.filter_by(username=username).first()
#
#     @staticmethod
#     def create(username, password_hash):
#         user = User(username=username, password_hash=password_hash)
#         db.session.add(user)
#         db.session.commit()
#         return user