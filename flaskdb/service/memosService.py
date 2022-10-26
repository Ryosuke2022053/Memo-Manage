from flask import session
from flaskdb.model.fileModel import File
from flaskdb.model.userModel import User


def insert_memos(data, file):
    username = session['username']
    user = User.query.filter_by(username=username).first()
    memo = File.query.filter_by(file_name=file).first()
    