# coding: utf-8
from flask import Flask, render_template
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint


app = Flask(__name__)
app.debug = True

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('common/404.html'), 404
