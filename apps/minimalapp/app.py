# Flaskクラスをimportする
from flask import Flask, render_template, url_for, request, redirect

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
# with app.test_request_context():
#     # /
#     print(url_for('index'))
#     # /hello/world
#     print(url_for('hello-endpoint', name='world'))
#     # /name/ichiro?page=1
#     print(url_for('show_name', name='ichiro', page=1))
    
# お問い合わせフォーム画面を表示する
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact/complete', methods=['GET', 'POST'])
def contact_complete():
    # POSTリクエストの場合のみ処理を行う
    if request.method == 'POST':
        # form属性を使ってフォームの値を取得する htmlのname属性を指定
        username = request.form['username']
        email = request.form['email']
        description = request.form['description']
        # メールを送る（最後に実装）
        
        # 自分自身にリダイレクトして、GETアクセスする
        return redirect(url_for('contact_complete'))
    # GETアクセスの場合は完了ページを表示する
    return render_template('contact_complete.html')