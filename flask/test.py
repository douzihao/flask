from flask import Flask,redirect,abort
from flask import request
from flask import make_response
from flask import render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    user_agent= request.headers.get('User-Agent')
    print request.headers.get("host")
    response = make_response('<p> your browser is sss </p>')
    response.set_cookie("ss",'33')
    return response
    #return '<p> your browser is %s </p>' %user_agent
    #return '<h1> hello world!</h1>'

@app.route('/testtem/<value>')
def testtem(value):
    return render_template("page.html")

@app.route('/ss/<kw>')
def ss(kw):
    return redirect("http://www.baidu.com")

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name

@app.route('/red')
def red():
    return redirect("http://www.baidu.com")

@app.route('/get_user/<id>')
def get_user(id):
    user = None
    if not user:
        abort(500)
    return ('<h1>hello</h1>')
if __name__=='__main__':
    manager.run()
    #app.run(debug=True,host='192.168.15.199')
