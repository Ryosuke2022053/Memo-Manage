from turtle import title
from flask import Blueprint, request, session, render_template, redirect, flash, url_for, Markup

from flaskdb import apps, db, da
from flaskdb.service.memoMDE import delete_md, write_md, read_md, read_edit_md
from flaskdb.service.mainForm import file_rename

memo_module = Blueprint("memo", __name__)


@memo_module.route("/view/<string:file>", methods=["GET"])
def memo_view(file):
    content = read_md(file)
    print(file)
    return render_template('memo/memo_view.html', md=content, file=file)


@memo_module.route("/edit/<string:file>", methods=["GET", "POST"])
def memo_edit(file):
    content = read_edit_md(file)
    if request.method == "POST":
      content = request.form["data"] 
      title = request.form["title"]
      if title != file:
        file_rename(file, title)
      write_md(content, title)
      return render_template("memo/memo_edit.html", data=content, file=title)
    else:
        return render_template("memo/memo_edit.html", data=content, file=file)


@memo_module.route("/add", methods=["GET", "POST"])
def memo_add():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["data"]    
        write_md(content, title)
        return render_template("memo/memo_add.html", data=content, file=title)
    else:
        return render_template("memo/memo_add.html", file="")

@memo_module.route("/delete/<string:file>", methods=["GET"])
def memo_delete(file):
    delete_md(file)
    return redirect(url_for("app.index"))
