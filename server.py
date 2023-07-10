
from flask_app.__init__ import app
from flask import Flask

import flask_app.index
import flask_app.views.blog.blog_main
import flask_app.views.mujiclo.mujiclo_main


app.secret_key = 'moon_server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

app = Flask(__name__, static_url_path='/static')