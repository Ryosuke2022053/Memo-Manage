from flask import Markup
from markdown import markdown
import os

def write_md(data, mdfile):
  with open('flaskdb/controller/view/article/' + mdfile + '.md', mode='w') as mdfile:
    mdfile.write(data)


def read_md(mdfile) -> str:
  with open('flaskdb/controller/view/article/' + mdfile + '.md', mode='r') as mdfile:
    mdcontent = mdfile.read()
    return Markup(markdown(mdcontent))


def read_edit_md(mdfile) -> str:
  with open('flaskdb/controller/view/article/' + mdfile + '.md', mode='r') as mdfile:
    mdcontent = mdfile.read()
    return mdcontent

def delete_md(mdfile):
  os.remove('flaskdb/controller/view/article/' + mdfile + '.md')
