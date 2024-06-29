from flask import Blueprint, render_template, redirect, url_for
from apps.crud.forms import UserForm
from apps.crud.models import User
from apps.app import db
from flask_login import login_required

# Blueprintでcrudアプリを生成する
crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static',
)

# indexエンドポイントを作成し、index.htmlを返す
@crud.route('/')
@login_required
def index():
    return render_template('crud/index.html')

# ユーザー新規登録画面
@crud.route('/users/new', methods=['GET', 'POST'])
@login_required
def create_user():
    # UserFormをインスタンス化する
    form = UserForm()
    # フォームの値をバリデートする
    if form.validate_on_submit():
        # ユーザーを作成する
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # ユーザーを追加してコミットする
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))
    return render_template('crud/create.html', form=form)

# ユーザー一覧画面
@crud.route('/users')
@login_required
def users():
    # ユーザー一覧を取得する
    users = User.query.all() # Userテーブルの全てのレコードを取得
    return render_template('crud/index.html', users=users) # users.htmlにusersを渡す

# ユーザー編集画面
@crud.route('users/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = UserForm()
    
    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()
    
    # formからサブミットされた場合はユーザーを更新しユーザー一覧画面へリダイレクトする
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users')) # ユーザー一覧画面へリダイレクトする
    
    # GETの場合は編集画面を表示する
    return render_template('crud/edit.html', user=user, form=form)

# ユーザー削除画面
@crud.route('/users/<user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()
    # ユーザーを削除する
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('crud.users')) # ユーザー一覧画面へリダイレクトする