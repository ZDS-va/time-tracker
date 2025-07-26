from flask import Blueprint, request, jsonify
from app.services.timelog_service import TimeLogService

bp = Blueprint('timelog_api', __name__, url_prefix='/api/timelogs')

@bp.route('/start', methods=['POST'])
def start_timelog():
    proj_id = (request.get_json() or {}).get('project_id')
    try:
        log = TimeLogService.start(proj_id)
        return jsonify(log.to_dict()), 201
    except LookupError as e:
        return jsonify({'error': str(e)}), 404
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/stop', methods=['POST'])
def stop_timelog():
    log_id = (request.get_json() or {}).get('id')
    try:
        log = TimeLogService.stop(log_id)
        return jsonify(log.to_dict()), 200
    except LookupError as e:
        return jsonify({'error': str(e)}), 404
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('', methods=['GET'])
def list_timelogs():
    proj_id = request.args.get('project_id', type=int)
    if not proj_id:
        return jsonify({'error': 'project_id 为必填'}), 400
    logs = TimeLogService.list_by_project(proj_id)
    return jsonify([l.to_dict() for l in logs])

@bp.route('/summary', methods=['GET'])
def summary_timelogs():
    proj_id = request.args.get('project_id', type=int)
    if not proj_id:
        return jsonify({'error': 'project_id 为必填'}), 400
    summary = TimeLogService.summary(proj_id)
    return jsonify({'project_id': proj_id, **summary})