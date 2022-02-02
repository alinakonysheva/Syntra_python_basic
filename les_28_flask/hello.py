from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

"""from flask_sqlalchemy import SQLAlchemy
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
)
app.config['Testing'] = True

db = SQLAlchemy(app)

"""