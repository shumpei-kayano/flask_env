from pathlib import Path # 追加
from flask import Flask
from flask_migrate import Migrate # 追加
from flask_sqlalchemy import SQLAlchemy # 追加

# SQLAlchemyインスタンス生成
db = SQLAlchemy()

# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    # アプリのコンフィグ設定をする
    app.config.from_mapping(
        SECRET_KEY='2AZSMss3p5QPbcY2hBj',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    
    # register_blueprintメソッドを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    
    return app