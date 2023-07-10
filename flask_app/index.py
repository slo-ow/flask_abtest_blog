from flask import render_template
from flask_app.__init__ import app

# /customer/customer_main/main.html
@app.route('/')
def index():
    return render_template('/customer/customer_main/main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
