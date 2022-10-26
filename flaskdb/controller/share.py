from crypt import methods
from flask import Blueprint, render_template, url_for, session, flash, redirect
from flaskdb.service.filesService import select_files, update_files
from flaskdb.service.shareMDE import share_read_md

share_module = Blueprint("share", __name__)

@share_module.route("/share")
def share_index():
    if not "username" in session:
        flash("もう一度ログインしてください。", "danger")
        return redirect(url_for("auth.login"))

    memo_list = select_files()
    return render_template('memoShare/share_index.html', mdfiles = memo_list)

@share_module.route("/share/view/<string:file>/<string:username>", methods=["GET"])
def share_view(file, username):
    if not "username" in session:
        flash("もう一度ログインしてください。", "danger")
        return redirect(url_for("auth.login"))
    content = share_read_md(username, file)
    return render_template('memoShare/share_view.html', md=content, file=file)

@share_module.route("/share/stop/<string:file>", methods=["GET"])
def share_stop(file):
    update_files(file, 0)
    return redirect(url_for('share.share_index'))
   