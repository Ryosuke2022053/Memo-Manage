from flask import Blueprint, request, session, render_template, redirect, flash, url_for
from flaskdb import apps, db, da
import datetime
from flaskdb.model.models import User
from flaskdb.service.LoginForm import LoginForm

auth_module = Blueprint("auth", __name__)

@auth_module.route("/now", methods=["GET", "POST"])
def now():
    return str(datetime.datetime.now())

@auth_module.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if user is None or user.password != form.password.data:
            flash("Username or Password is incorrect.", "danger")
            return redirect(url_for("auth.login"))

        session["username"] = user.username
        return redirect(url_for("app.index"))

    return render_template("auth/login.html", form=form)

@auth_module.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None)
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("app.index"))