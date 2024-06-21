from flask import Flask

# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    
    # register_blueprintメソッドを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    
    return app