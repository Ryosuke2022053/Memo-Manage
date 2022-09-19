from flaskdb.model.memoModel import Memo
from flaskdb import db

def insert_memo(file, id, username):
    memo = Memo()
    memo.file_name = file
    memo.user_id = id
    memo.user_name = username
    memo.share = 1
    db.session.add(memo)
    db.session.commit()

