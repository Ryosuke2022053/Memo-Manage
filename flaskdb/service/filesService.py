from flask import session
from flaskdb.model.fileModel import File
from flaskdb.model.userModel import User
import datetime
from flaskdb import db

def insert_files(file, num):
    memo = File()
    username = session["username"]
    user = User.query.filter_by(username=username).first()
    memo.file_name = file
    memo.user_id = user.id
    memo.user_name = username
    memo.share = num
    memo.updated_at = datetime.datetime.now()
    db.session.add(memo)
    db.session.commit()

def select_files():
    memo_list = File.query.filter(File.share == 1).all()
    for i in range(len(memo_list)):
        days = memo_list[i].updated_at.strftime('%Y/%m/%d %H:%M')
        memo_list[i].updated_at = days
    return memo_list

def select_all_files():
    memo_list = File.query.order_by(File.id.asc()).all()
    return memo_list

def delete_files(file):
    memo_id = File.query.filter(File.user_name == session["username"] , File.file_name == file).one()
    db.session.delete(memo_id)
    db.session.commit()

def update_files(file, num):
    memo = File.query.filter(File.user_name == session["username"] , File.file_name == file).one()
    memo.share = num
    db.session.commit()

def update_edit_files(file, title):
    memo = File.query.filter(File.user_name == session["username"] , File.file_name == file).one()
    memo.updated_at = datetime.datetime.now()
    memo.file_name = title
    db.session.commit()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
