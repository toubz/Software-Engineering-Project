from flask import Flask, render_template, request
from .locale.traveler import traveler
from .locale.local import local
from .locale.forms import SignUpForm

app = Flask(__name__)
app.register_blueprint(traveler)
app.register_blueprint(local)
app.config['SECRET_KEY'] = "3P/j+YlCGbjOp~'KNnp#JC[GbV`]{y"
app.config['WTF_CSRF_SECRET_KEY'] = "PWa~DxHcGZxI[SmI0UDa@3l1fYlxx"

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/index', methods=('GET', 'POST'))
def submit():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)


