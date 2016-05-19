from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name
def index():
    return '<h1> hello world!</h1>'
if __name__=='__main__':
    app.run(debug=True)
