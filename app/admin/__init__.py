# coding: utf-8
from flask import Blueprint


admin = Blueprint('admin', __name__)

# 这里不能把import放在顶部，因为views里引用了admin，所以应该先创建admin实例
import app.admin.views
