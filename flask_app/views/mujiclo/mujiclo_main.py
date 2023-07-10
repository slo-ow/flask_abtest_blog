from flask import jsonify, request, render_template, make_response, session, current_app
from flask_app.__init__ import app
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from flask_app.views.blog import blog_main
from flask_app.blog_control.user_mgmt import User

import os


# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

CORS(app)

app.register_blueprint(blog_main.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


#
@app.route("/member")
def member():
    return render_template('/customer/customer_member/member.html')
#
@app.route("/board")
def board():
    return render_template('/customer/customer_board/board.html')
#
@app.route("/contact")
def contact():
    return render_template('/customer/customer_contact/contact.html')
#
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
#
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)
#
@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get(
            'HTTP_X_REAL_IP', request.remote_addr)
