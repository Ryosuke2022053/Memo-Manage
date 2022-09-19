from flask import session
from flaskdb.model.memoModel import Memo
from flaskdb.model.userModel import User
import datetime
from flaskdb import db

def insert_memo(file):
    memo = Memo()
    username = session["username"]
    user = User.query.filter_by(username=username).first()
    memo.file_name = file
    memo.user_id = user.id
    memo.user_name = username
    memo.share = 1
    memo.updated_at = datetime.datetime.now()
    db.session.add(memo)
    db.session.commit()

def select_memo():
    memo_list = Memo.query.all()
    for i in range(len(memo_list)):
        days = memo_list[i].updated_at.strftime('%Y/%m/%d %H:%M')
        memo_list[i].updated_at = days
    return memo_list