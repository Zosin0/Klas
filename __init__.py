from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'Klas'



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'projetinho'
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = 'C:\\temp\\Klas\\Klas\\static\\imagens'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/Klas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)




    from main import main


    app.register_blueprint(main, url_prefix='/')


    from classes import User


    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_user):
        return User.query.get(int(id_user))


    return app



def create_database(app):
    if not path.exists('Klas/' + DB_NAME):
        db.create_all(app=app)
