from crypt import methods
from turtle import title
from flask import Blueprint, request, session, render_template, redirect, flash, url_for, Markup

from flaskdb import apps, db, da
from flaskdb.model.userModel import User
from flaskdb.service.memoMDE import memo_MDE
from flaskdb.model.memoModel import Memo
from flaskdb.service.mainService import file_rename, file_name_list
from flaskdb.service.memoService import insert_memo

memo_module = Blueprint("memo", __name__)


@memo_module.route("/view/<string:file>", methods=["GET"])
def memo_view(file):
    content = memo_MDE(file).read_md()
    return render_template('memo/memo_view.html', md=content, file=file)


@memo_module.route("/edit/<string:file>", methods=["GET", "POST"])
def memo_edit(file):
    content = memo_MDE(file).read_edit_md()
    if request.method == "POST":
        content = request.form["data"] 
        title = request.form["title"]
        # ファイル名変更チェック
        if title != file:
            # 重複チェック
            mdfile_list = file_name_list()
            if title in mdfile_list:
                memo_MDE(file).write_md(content)
                return render_template("memo/memo_edit.html", data=content, file=file, errortext = True)    
            
            file_rename(file, title)
        memo_MDE(title).write_md(content)
        return render_template("memo/memo_edit.html", data=content, file=title)
    else:
        return render_template("memo/memo_edit.html", data=content, file=file)


@memo_module.route("/add", methods=["GET", "POST"])
def memo_add():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["data"] 
        mdfile_list = file_name_list()
        if title in mdfile_list:
            return render_template("memo/memo_add.html", data=content, file="", errortext = True)
        memo_MDE(title).write_md(content)
        return redirect(url_for("app.index"))
    else:
        return render_template("memo/memo_add.html", file="")


@memo_module.route("/delete/<string:file>", methods=["GET"])
def memo_delete(file):
    memo_MDE(file).delete_md()
    return redirect(url_for("app.index"))

@memo_module.route("/share/<string:file>", methods=["GET"])
def memo_share(file):
    if not "username" in session:
        return redirect(url_for("auth:login"))
    username = session["username"]
    user = User.query.filter_by(username=username).first()
    insert_memo(file, user.id, username)
    return redirect(url_for("app.index"))
    