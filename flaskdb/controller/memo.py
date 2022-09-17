from flask import Blueprint, request, session, render_template, redirect, flash, url_for, Markup

from flaskdb import apps, db, da
from flaskdb.model.models import User
from markdown import markdown

memo_module = Blueprint("memo", __name__)


def read_md() -> str:
  with open('flaskdb/controller/view/article/sample1.md', mode='r') as mdfile:
    mdcontent = mdfile.read()

  return Markup(markdown(mdcontent))


@memo_module.route("/memo")
def memoViewer():
    content = read_md()
    return render_template('memo.html', md=content)
