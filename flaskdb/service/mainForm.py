import os

def file_name_list():
    mdfile_list = []
    current_dir = os.getcwd()
    mdfile = os.path.join(current_dir,'flaskdb','controller','view', 'article')
    mdfiles = os.listdir(mdfile)
    for path in mdfiles:
        file = os.path.splitext(path)[0]
        mdfile_list.append(file)
    return mdfile_list
