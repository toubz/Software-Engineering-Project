#! /usr/bin/python3.7
from flask import Flask, render_template, request, redirect, url_for
from .itinerista.traveler import traveler
from .itinerista.local import local
from .itinerista.forms import SignUpForm

app = Flask(__name__)
app.register_blueprint(traveler)
app.register_blueprint(local)
app.config['SECRET_KEY'] = "3P/j+YlCGbjOp~'KNnp#JC[GbV`]{y"
app.config['WTF_CSRF_SECRET_KEY'] = "PWa~DxHcGZxI[SmI0UDa@3l1fYlxx"

@app.route('/', methods=['GET', 'POST'])
def submit():
    form = SignUpForm()
    if form.validate_on_submit():
        if (form.travelerSubmit.data):
            # This is where we will add to database
            # Lets wait for that to be setup


            return redirect(url_for('traveler.traveler_dashboard'))
        elif (form.localSubmit.data):
            # Here too

            return redirect(url_for('local.local_dashboard'))
    return render_template('index.html', form=form)
