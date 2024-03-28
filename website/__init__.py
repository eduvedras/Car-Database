from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="eduvedras",
    password="hjshjhdjah kjshkjdhjs",
    hostname="eduvedras.mysql.pythonanywhere-services.com",
    databasename="eduvedras$database1",
)
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app


