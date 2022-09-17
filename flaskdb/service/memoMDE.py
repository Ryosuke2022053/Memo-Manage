from flask import Markup
from markdown import markdown


def write_md(data):
  with open('./article/main.md', mode='w') as mdfile:
    mdfile.write(data)


def add_md(data):
  with open('./article/add.md', mode='w') as mdfile:
    mdfile.write(data)


def read_md(mdfile) -> str:
  with open('flaskdb/controller/view/article/' + mdfile, mode='r') as mdfile:
    mdcontent = mdfile.read()
    return Markup(markdown(mdcontent))

def read_edit_md(mdfile) -> str:
  with open('flaskdb/controller/view/article/' + mdfile, mode='r') as mdfile:
    mdcontent = mdfile.read()
    return mdcontent