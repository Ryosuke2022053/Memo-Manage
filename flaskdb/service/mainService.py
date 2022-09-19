import os
from flask import session

def create_private_folder(username):
        current_dir = os.getcwd()
        mdfile = os.path.join(current_dir, 'flaskdb', 'article_private')
        path = mdfile + '/' + username
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path, exist_ok=True)


def public_dir():
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir, 'flaskdb', 'article_public')
    return mdfile


def private_dir(username):
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir, 'flaskdb', 'article_private', username)
    return mdfile


def file_name_list(now):
    mdfile_list = []
    if now == "public":
        mdfile = public_dir()
    else:
        username = session["username"]
        mdfile = private_dir(username)
    mdfiles = os.listdir(mdfile)
    for path in mdfiles:
        file = os.path.splitext(path)[0]
        mdfile_list.append(file)
    mdfiles_list = sorted(mdfile_list)
    return mdfiles_list
    

def file_rename(before_title, after_title):
    before_file = public_dir() + '/' + before_title + '.md'
    after_file = public_dir() + '/' + after_title + '.md' 
    os.rename(before_file, after_file)

