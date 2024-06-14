# Flaskクラスをimportする
from flask import Flask, render_template, url_for

# Flaskクラスのインスタンス化する
app = Flask(__name__)

# URLと実行する関数をマッピングする
@app.route('/')
def index():
    return 'Hello, Flaskbook!'

@app.route('/hello/<name>', methods=['GET', 'POST'], endpoint='hello-endpoint')
def hello(name): # URLパラメータのnameを受け取る
    return f'Hello, {name}!'

# show_nameエンドポイントを作成する
@app.route('/name/<name>')
def show_name(name):
    return render_template('index.html', name=name)

# url_for関数を使ってURLを生成する
with app.test_request_context():
    # /
    print(url_for('index'))
    # /hello/world
    print(url_for('hello-endpoint', name='world'))
    # /name/ichiro?page=1
    print(url_for('show_name', name='ichiro', page=1))