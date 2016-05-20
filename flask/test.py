from flask import Flask,redirect,abort
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1> hello world!</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' %name
@app.route('/red')
def red():
    return redirect("http://www.baidu.com")        
@app.route('/get_user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return ('<h1>hello</h1>')
if __name__=='__main__':
    app.run(debug=True,host='192.168.8.140')
