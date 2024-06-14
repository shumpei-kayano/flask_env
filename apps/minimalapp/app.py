# Flaskクラスをimportする
from flask import Flask

# Flaskクラスのインスタンス化する
app = Flask(__name__)

# URLと実行する関数をマッピングする
@app.route('/')
def index():
    return 'Hello, Flaskbook!'

@app.route('/hello', methods=['GET'], endpoint='hello-endpoint')
def hello():
    return 'Hello, World!'