
from flask import Flask

import app.routes.auth_route as auth_route
import app.routes.tasks_route as tasks_route
import app.routes.drones_route as drones_route


def set_routes(app: Flask):
    app.register_blueprint(auth_route.auth_bp)
    app.register_blueprint(tasks_route.tasks_bp)
    app.register_blueprint(drones_route.drones_bp)
