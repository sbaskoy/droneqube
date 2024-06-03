

from app.schemas import db
from app.schemas.Task import Task


class TaskRepository:
    @staticmethod
    def get_all_tasks():
        return Task.query.all()

    @staticmethod
    def paginate(page: int, per_page: int):
        return Task.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_task_by_id(id: int):
        return Task.query.get(id)

    @staticmethod
    def add_task(task: Task):
        db.session.add(task)
        db.session.commit()

    @staticmethod
    def update_task(task: Task):
        db.session.commit()

    @staticmethod
    def delete_task(task: Task):
        db.session.delete(task)
        db.session.commit()
