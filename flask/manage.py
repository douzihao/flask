from flask.ext.script import Manager
from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/user/<name>')
def user():
    return render_template("index.html")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
if __name__ == '__main__':
    manager.run()
