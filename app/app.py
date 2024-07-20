from flask import Flask #importing flask from flask
from .config import Config #importing config
from .routes import employees_bp #importing employees_bp from .routes
from .db_instance import db #importing db from .db_instance
from .error import errors #importing errors from .error
#defining a function create_app
def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(employees_bp, url_prefix='/api')
    app.register_blueprint(errors)

    return app 