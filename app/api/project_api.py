from flask import Blueprint, request, jsonify
from app.services.project_service import ProjectService

bp = Blueprint('project_api', __name__, url_prefix='/api/projects')

@bp.route('', methods=['GET'])
def get_projects():
    projs = ProjectService.list_all()
    return jsonify([p.to_dict() for p in projs])

@bp.route('', methods=['POST'])
def post_project():
    data = request.get_json() or {}
    try:
        proj = ProjectService.create(data.get('name', '').strip(), data.get('category_id'))
        return jsonify(proj.to_dict()), 201
    except (ValueError, LookupError) as e:
        code = 400 if isinstance(e, ValueError) else 404
        return jsonify({'error': str(e)}), code