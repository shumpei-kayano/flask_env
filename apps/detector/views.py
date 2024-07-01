from flask import Blueprint, render_template

# template_folderを指定する
dt = Blueprint('dt', __name__, template_folder='templates')

# dtアプリのエンドポイントを作成する
@dt.route('/')
def index():
    return render_template('detector/index.html')