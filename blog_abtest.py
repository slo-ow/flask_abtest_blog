from flask import Flask, jsonify, request, render_template, make_response, session, current_app
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
from blog_control.user_mgmt import User
from flask_googlemaps import GoogleMaps, Map
from flask_qrcode import QRcode

import os


# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'dave_server3'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

# you can add your Google Maps API key here
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBLLp7r6pTKP48trkoQy8v2boesLXvstCc"

GoogleMaps(app)

#
qrcode = QRcode(app)

#
@app.route('/main')
def index():
    return render_template('main.html')
#
@app.route("/member")
def member():
    return render_template('member.html')
#
@app.route("/board")
def board():
    return render_template('board.html')
#
@app.route("/contact")
def contact():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1430,
        markers=[(35.688672659335104, 139.70176049718648)]
    )
    return render_template('contact.html', mymap=mymap)
#
@app.route("/qrcode")
def qrcode():
    # qrcode_url = "https://72f9-2404-7a80-82c0-5d10-5d4d-5cd5-df5e-c8ef.ngrok-free.app/main"
    qrcode_url = "https://www.mynavi.jp"
    return render_template('qrcode.html', qrcode_url=qrcode_url)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get(
            'HTTP_X_REAL_IP', request.remote_addr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
