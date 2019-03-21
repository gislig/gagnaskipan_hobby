import pymssql
import json
from models.supporters_model import (
    SupporterList
)

from flask import (
    Flask,
    render_template,
    jsonify
)

server = "localhost"
user = "hobby"
password = "Gagnaskipan.123"
database = "supporters"

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    cl = SupporterList()
    supportlist = cl.get_all(cursor)
    return render_template("home.html",supportlist=supportlist)

@app.route('/supporters')
def supporters():
    cl = SupporterList()
    return cl.get_all(cursor)

if __name__ == '__main__':
    app.run(debug=False, port=80)