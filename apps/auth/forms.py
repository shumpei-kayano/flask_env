from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# サインアップ用のフォームクラスを作成
class SignUpForm(FlaskForm):
    username = StringField(
        'ユーザー名',
        validators=[
            DataRequired('ユーザー名は必須です。'),
            Length(1, 30, '0文字以内で入力してください。'),
            ],
        )
    email = StringField(
        'メールアドレス',
        validators=[
            DataRequired('メールアドレスは必須です。'),
            Email('メールアドレスの形式で入力してください。'),
            ],
        )
    password = PasswordField(
        'パスワード',
        validators=[DataRequired("パスワードは必須です。")]
        )
    submit = SubmitField('新規登録')

# ログイン用のフォームクラスを作成
class LoginForm(FlaskForm):
    email = StringField(
        'メールアドレス',
        validators=[
            DataRequired('メールアドレスは必須です。'),
            Email('メールアドレスの形式で入力してください。'),
            ],
        )
    password = PasswordField(
        'パスワード',
        validators=[DataRequired("パスワードは必須です。")]
        )
    submit = SubmitField('ログイン')