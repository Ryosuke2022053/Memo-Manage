"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask import Flask
apps = Flask(__name__, static_folder="controller/view/static", template_folder="controller/view/templates")
apps.config.from_object("flaskdb.config")

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(apps)

from flaskdb.repository.dataaccess import DataAccess
import flaskdb.var as v
da = DataAccess(v.HOSTNAME, v.PORT, v.DBNAME, v.USERNAME, v.PASSWORD)

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(apps)

from flask_bootstrap import Bootstrap
bs = Bootstrap(apps)

from flaskdb.controller.views import app
from flaskdb.controller.auth import auth_module
from flaskdb.controller.item import item_module
from flaskdb.controller.memo import memo_module

apps.register_blueprint(app)
apps.register_blueprint(auth_module)
apps.register_blueprint(item_module)
apps.register_blueprint(memo_module)
