# from . import db
# from datetime import datetime
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def to_dict(self):
#         return {'id': self.id, 'username': self.username}