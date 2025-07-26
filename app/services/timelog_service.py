from app.models.timelog import TimeLog
from app.models.project import Project
from app.extension import db
from datetime import datetime

class TimeLogService:
    @staticmethod
    def start(project_id):
        if not Project.query.get(project_id):
            raise LookupError('项目不存在')
        existing = TimeLog.query.filter_by(project_id=project_id, end_time=None).first()
        if existing:
            raise RuntimeError('已有进行中的记录')
        log = TimeLog(project_id=project_id, start_time=datetime.utcnow())
        db.session.add(log)
        db.session.commit()
        return log

    @staticmethod
    def stop(log_id):
        log = TimeLog.query.get(log_id)
        if not log:
            raise LookupError('记录不存在')
        if log.end_time:
            raise RuntimeError('记录已结束')
        log.end_time = datetime.utcnow()
        db.session.commit()
        return log

    @staticmethod
    def list_by_project(project_id):
        return TimeLog.query.filter_by(project_id=project_id).order_by(TimeLog.start_time.desc()).all()

    @staticmethod
    def summary(project_id):
        logs = TimeLog.query.filter_by(project_id=project_id).filter(TimeLog.end_time.isnot(None)).all()
        total_sec = sum((l.end_time - l.start_time).total_seconds() for l in logs)
        return {'total_seconds': total_sec, 'total_hours': round(total_sec/3600, 2)}