from flask import Blueprint, session, render_template, redirect, flash, url_for
from flaskdb import db

from flaskdb.model.itemModel import Item
from flaskdb.model.userModel import User
from flaskdb.controller.form.ItemForm import AddItemForm, SearchItemForm

item_module = Blueprint("item", __name__)

@item_module.route("/additem", methods=["GET", "POST"])
def additem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("auth.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        db.session.add(item)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("item.additem"))

    itemlist = Item.query.all()
    return render_template("item/additem.html", form=form, itemlist=itemlist)

@item_module.route("/searchitem", methods=["GET", "POST"])
def searchitem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("auth.login"))

    form = SearchItemForm()

    if form.validate_on_submit():
        itemlist = Item.query.filter(Item.itemname.like("%" + form.itemname.data + "%")).all()
        return render_template("item/search.html", form=form, itemlist=itemlist)

        # For change to PRG
        # itemlist = pickle.dumps(itemlist)
        # session["itemlist"] = itemlist
        # return redirect(url_for("app.searchitem"))

    # if "itemlist" in session:
    #     itemlist = session["itemlist"]
    #     itemlist = pickle.loads(itemlist)
    #     session.pop("itemlist", None)
    # else:
    #     itemlist = None
    #
    # return render_template("search.html", form=form, itemlist=itemlist)

    return render_template("item/search.html", form=form)