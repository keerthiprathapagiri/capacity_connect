import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from config import Config

db=SQLAlchemy(); login_manager=LoginManager(); socketio=SocketIO(async_mode='threading', cors_allowed_origins='*')

def create_app(config_class=Config):
    app=Flask(__name__); app.config.from_object(config_class)
    for p in (app.config['UPLOAD_VIDEO_FOLDER'], app.config['UPLOAD_TRANSCRIPT_FOLDER'], app.instance_path): os.makedirs(p,exist_ok=True)
    db.init_app(app); login_manager.init_app(app); socketio.init_app(app)
    login_manager.login_view='auth.login'
    from models import User
    @login_manager.user_loader
    def load_user(uid): return db.session.get(User,int(uid))
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.courses import courses_bp
    from routes.learner import learner_bp
    from routes.trainer import trainer_bp
    from routes.admin import admin_bp
    from routes.doubts import doubts_bp
    from routes.api import api_bp
    for bp in [auth_bp,main_bp,courses_bp,learner_bp,trainer_bp,admin_bp,doubts_bp,api_bp]: app.register_blueprint(bp)
    from routes.chat import register_chat
    register_chat(socketio)
    with app.app_context(): db.create_all()
    return app

app=create_app()
if __name__=='__main__': socketio.run(app,debug=True)
