from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService

bp = Blueprint('category_api', __name__, url_prefix='/api/categories')

@bp.route('', methods=['GET'])
def get_categories():
    cats = CategoryService.list_all()
    return jsonify([c.to_dict() for c in cats])

@bp.route('', methods=['POST'])
def post_category():
    name = (request.get_json() or {}).get('name', '').strip()
    try:
        cat = CategoryService.create(name)
        return jsonify(cat.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400