from flask import Blueprint, render_template

local = Blueprint('local', __name__, template_folder='templates')

@local.route("/local/dashboard/")
def local_dashboard():
    return render_template('local_dashboard.html')