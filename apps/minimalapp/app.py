# Flaskクラスをimportする
from flask import Flask

# Flaskクラスのインスタンス化する
app = Flask(__name__)

# URLと実行する関数をマッピングする
@app.route('/')
def index():
    return 'Hello, Flaskbook!'

@app.route('/hello')
def hello():
    return 'Hello, World!'