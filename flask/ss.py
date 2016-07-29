from flask.ext.script import  Manager
from flask import Flask
app = Flask(__name__)
manage = Manager(app)

if __name__ == '__main__':
    manage.run()
