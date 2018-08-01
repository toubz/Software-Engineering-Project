from flask import Flask, render_template, request
from locale.traveler import traveler
from locale.local import local

app = Flask(__name__)
app.register_blueprint(traveler)
app.register_blueprint(local)

@app.route("/")
def main():
    return render_template("index.html")
