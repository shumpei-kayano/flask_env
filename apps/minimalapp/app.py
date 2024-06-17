from email_validator import validate_email, EmailNotValidError
import os
from flask_mail import Mail, Message
from flask import (
    Flask,
    current_app,
    g,
    render_template,
    url_for, 
    request,
    redirect,
    flash,
)

# Flaskクラスのインスタンス化する
app = Flask(__name__)
# SECRET_KEYを追加する
app.config['SECRET_KEY'] = '2AZSMss3p5QPbcY2hBsJ'

# Mailクラスのコンフィグを追加する
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

# flask-mail拡張を登録する
mail = Mail(app)

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
        
        # 入力チェック バリデーションフラグをデフォルトTrueにしておく
        is_valid = True
        if not username: # ユーザ名が空の場合
            flash('ユーザ名は必須です。')
            is_valid = False
            
        if not email: # メールアドレスが空の場合
            flash('メールアドレスは必須です。')
            is_valid = False
        try: # メールアドレスの形式チェック
            validate_email(email)
        except EmailNotValidError:
            flash('メールアドレスの形式で入力してください。')
            is_valid = False
        
        if not description: # お問い合わせ内容が空の場合
            flash('お問い合わせ内容は必須です。')
            is_valid = False

        # バリデーションエラーがある場合はフォーム画面に戻る
        if not is_valid:
            return redirect(url_for('contact'))
        
        # メールを送る（最後に実装）
        send_mail(email,"問い合わせありがとうございました", "contact_mail", username=username, description=description)
        
        # 自分自身にリダイレクトして、GETアクセスする
        flash('問い合わせ内容はメールにて送信しました。問い合わせありがとうございました。')
        return redirect(url_for('contact_complete'))
    # GETアクセスの場合は完了ページを表示する
    return render_template('contact_complete.html')

# send_mail関数を作成する
def send_mail(to, subject, template, **kwargs):
    # メールを送信する
    msg = Message(subject, recipients=[to])
    msg.body = render_template(f'{template}.txt', **kwargs)
    msg.html = render_template(f'{template}.html', **kwargs)
    mail.send(msg)