from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = 'Klas'
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'projetinho'
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = 'C:\\temp\\Klas\\Klas\\static\\imagens'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/Klas'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'projetoceub@gmail.com'
    app.config['MAIL_PASSWORD'] = 'okclnmbvgopxiamc'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    from main import main

    app.register_blueprint(main, url_prefix='/')


    from classes import User




    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_user):
        return User.query.get(int(id_user))
    return app

