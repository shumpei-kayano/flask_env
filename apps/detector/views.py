from apps.app import db
from apps.crud.models import User
from apps.detector.models import UserImage
from flask import Blueprint, render_template, current_app, send_from_directory

# template_folderを指定する
dt = Blueprint('dt', __name__, template_folder='templates')

# dtアプリのエンドポイントを作成する
@dt.route('/')
def index():
    # UserとUserImageをJoinして画像一覧を取得する
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    
    return render_template('detector/index.html', user_images=user_images)

@dt.route('/images/<path:filename>')
def image_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)