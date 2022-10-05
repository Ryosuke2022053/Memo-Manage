import os
from flask import session

def create_private_folder(username):
        current_dir = os.getcwd()
        dir_list = [[current_dir,'flaskdb', 'article_private'], [current_dir,'flaskdb', 'controller', 'view', 'static', 'attachments']]
        for dir in dir_list:
            mdfile = os.path.join(*dir)
            path = mdfile + '/' + username
            if os.path.exists(path):
                pass
            else:
                os.makedirs(path, exist_ok=True)


def private_dir(username):
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir, 'flaskdb', 'article_private', username)
    return mdfile


def file_name_list():
    mdfile_list = []
    username = session["username"]
    mdfile = private_dir(username)
    mdfiles = os.listdir(mdfile)
    for path in mdfiles:
        file = os.path.splitext(path)[0]
        mdfile_list.append(file)
    mdfiles_list = sorted(mdfile_list)
    return mdfiles_list
    

def private_file_rename(before_title, after_title):
    before_file = private_dir(session["username"]) + '/' + before_title + '.md'
    after_file = private_dir(session["username"]) + '/' + after_title + '.md' 
    os.rename(before_file, after_file)
