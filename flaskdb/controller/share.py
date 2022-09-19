from flask import Blueprint, render_template, url_for
from flaskdb.service.memoService import select_memo

share_module = Blueprint("share", __name__)

@share_module.route("/share")
def share_index():
    memo_list = select_memo()
    return render_template('memoShare/share_index.html', mdfiles = memo_list)

