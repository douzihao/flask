from flask import Flask,redirect,abort
from flask import request
from flask import make_response
from flask import render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextField,validators
from wtforms.validators import DataRequired


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class NameForm(Form):
    name = StringField('your name',[validators.DataRequired()])
    #user = TabError("ss",[validators.length(min=4,max=20),validators.DataRequired])
    submit = SubmitField('submit')

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])

app = Flask(__name__)
app.config["SECRET_KEY"]='test'
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
    #return render_template("page.html")
    return render_template("page.html",current_time=datetime.utcnow())


@app.route('/ss/<kw>')
def ss(kw):
    return redirect("http://www.baidu.com")


@app.route('/user/<name>',methods=['GET','POST'])
def user(name):
    name = None
    nameForm = NameForm()
    if nameForm.validate_on_submit():
        name = nameForm.name.data
        nameForm.name.data = ''
    return render_template("index.html",form=nameForm,name=name)


@app.route('/red')
def red():
    return redirect("http://www.baidu.com")


@app.route('/get_user/<id>')
def get_user(id):
    user = None
    if not user:
        abort(500)
    return ('<h1>hello</h1>')

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('test.html', form=form)

if __name__=='__main__':
    manager.run()
    #app.run(debug=True,host='192.168.15.199')
