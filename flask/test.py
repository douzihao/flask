from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/user/<name>')
@app.route('/sytest/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name
def sytest(name):
    return '<h1>hello,%s!</h1>' %name
def index():
    return '<h1> hello world!</h1>'
if __name__=='__main__':
    app.run(debug=True)
