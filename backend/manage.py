from flask_script import Manager
from flask_migrate import MigrateCommand
from app import app
from app.schemas import db


manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
