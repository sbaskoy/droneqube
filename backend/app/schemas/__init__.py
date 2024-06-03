from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db: SQLAlchemy = SQLAlchemy()

migrate = Migrate()


def init(app: Flask):
    print("Database init")
    # migrate.init_app(app=app, db=db)
    db.init_app(app)
    db.create_all()
