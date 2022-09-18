import os

from flaskdb.controller.auth import now

def now_dir():
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir,'flaskdb','controller','view', 'article')
    return mdfile

def file_name_list():
    mdfile_list = []
    mdfile = now_dir()
    mdfiles = os.listdir(mdfile)
    for path in mdfiles:
        file = os.path.splitext(path)[0]
        mdfile_list.append(file)
    return mdfile_list

def file_rename(before_title, after_title):
    mdfile = now_dir()
    before_file = now_dir() + '/' + before_title + '.md'
    after_file = now_dir() + '/' + after_title + '.md' 
    os.rename(before_file, after_file)
