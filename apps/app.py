from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
import os

# SQLAlchemyインスタンス生成
db = SQLAlchemy()

csrf = CSRFProtect()

# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    config_key = os.getenv('FLASK_CONFIG', 'local')
    # config_keyにマッチする環境のコンフィグクラスを読み込む
    app.config.from_object(config[config_key])
    
    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    
    csrf.init_app(app)
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    
    # register_blueprintメソッドを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    
    return app