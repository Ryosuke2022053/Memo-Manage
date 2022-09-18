from flaskdb.model.memoModel import Memo
from flaskdb import db

def insert_memo(file, id):
    memo = Memo()
    memo.user_id = id
    memo.file_name = file
    memo.share = 1
    db.session.add(memo)
    db.session.commit()
