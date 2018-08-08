from flask import Blueprint, render_template

traveler = Blueprint('traveler', __name__, template_folder='templates')

@traveler.route("/traveler/dashboard/")
def traveler_dashboard():
    return render_template('traveler_dashboard.html')
