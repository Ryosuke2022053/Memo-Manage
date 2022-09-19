import os

from flaskdb.controller.auth import now

def public_dir():
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir, 'flaskdb', 'article_public')
    return mdfile

def private_dir():
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir, 'flaskdb', 'article_private')
    return mdfile

def file_name_list(now):
    mdfile_list = []
    if now == "public":
        mdfile = public_dir()
    else:
        mdfile = private_dir()
    mdfiles = os.listdir(mdfile)
    for path in mdfiles:
        file = os.path.splitext(path)[0]
        mdfile_list.append(file)
    mdfiles_list = sorted(mdfile_list)
    return mdfiles_list

def file_rename(before_title, after_title):
    mdfile = public_dir()
    before_file = public_dir() + '/' + before_title + '.md'
    after_file = public_dir() + '/' + after_title + '.md' 
    os.rename(before_file, after_file)

