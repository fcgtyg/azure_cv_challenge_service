from flask import Flask, request
from . import db
app = Flask(__name__)

@app.route("/", methods=["GET", "UPDATE"])
def hello_world():
    if request.method == "GET":
        return {"count": db.get_visitor_count()}
    else:
        db.update_visitor_count()
        return