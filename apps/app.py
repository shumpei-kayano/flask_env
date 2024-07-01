from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager
import os

# SQLAlchemyインスタンス生成
db = SQLAlchemy()

csrf = CSRFProtect()

# LoginManagerをインスタンス化する
login_manager = LoginManager()
# 未ログイン時にリダイレクトするエンドポイントを設定する
login_manager.login_view = 'auth.signup'
# ログイン後に表示するメッセージを指定する
# ここでは何も表示しないように空を指定する
login_manager.login_message = ''

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
    # login_managerとアプリを連携する
    login_manager.init_app(app)
    
    csrf.init_app(app)
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    # authパッケージからviewsをインポートする
    from apps.auth import views as auth_views
    # detectorパッケージからviewsをインポートする
    from apps.detector import views as dt_views
    
    # register_blueprintメソッドを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    # register_blueprintメソッドを使いviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    # register_blueprintメソッドを使いviewsのdtをアプリへ登録する
    app.register_blueprint(dt_views.dt)
    
    return app