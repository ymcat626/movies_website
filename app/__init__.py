# coding: utf-8
from flask import Flask, render_template

import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost/movie'  # python3中要使用pymysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '7f7e727930bb41109c6a0f4cc90d5f4b'

app.debug = True
db = SQLAlchemy(app)  # 这块不能写在蓝图底下，不然会因为调用顺序问题报错

from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('common/404.html'), 404
