from crypt import methods
from operator import methodcaller
from flask import Blueprint, request, session, render_template, redirect, flash, url_for, Markup

from flaskdb import apps, db, da
from flaskdb.model.models import User
from flaskdb.service.memoMDE import write_md, add_md, read_md, read_edit_md
from markdown import markdown

memo_module = Blueprint("memo", __name__)


@memo_module.route("/view/<string:file>", methods=["GET"])
def memo_view(file):
    content = read_md(file)
    print(file)
    return render_template('memo/memo_view.html', md=content)

@memo_module.route("/edit/<string:file>", methods=["GET", "POST"])
def memo_edit(file):
    content = read_edit_md(file)
    if request.method == "POST":
      content = request.form["data"]
      print(content)
      write_md(content)
      return render_template("memo/memo_edit.html", data=content, file=file)
    else:
        return render_template("memo/memo_edit.html", data=content, file=file)

