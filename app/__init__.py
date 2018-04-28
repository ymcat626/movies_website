# coding: utf-8
from flask import Flask, render_template
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost/movie'  # python3中要使用pymysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True

db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('common/404.html'), 404
