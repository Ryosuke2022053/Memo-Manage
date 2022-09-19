from flask import Blueprint, render_template, url_for
from flaskdb.service.mainService import file_name_list

share_module = Blueprint("share", __name__)

@share_module.route("/share")
def share_index():
    mdfile_list = file_name_list()
    return render_template('memoShare/share_index.html', mdfiles = mdfile_list)

