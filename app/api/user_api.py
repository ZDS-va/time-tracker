# from flask import Blueprint, request, jsonify
# from app.services.user_service import UserService
#
# bp = Blueprint('user_api', __name__, url_prefix='/api/users')
#
# @bp.route('/<username>', methods=['GET'])
# def get_user(username):
#     user = UserService.get_by_username(username)
#     if not user:
#         return jsonify({'error': '用户不存在'}), 404
#     return jsonify(user.to_dict())