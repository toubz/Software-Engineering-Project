from flask import Blueprint, Flask, render_template, request, redirect, url_for
from .forms import CreateRequestForm

traveler = Blueprint('traveler', __name__, template_folder='templates')

# Brings traveler to their home page
@traveler.route("/traveler/dashboard/")
def traveler_dashboard():
    # Create a request
    form = CreateRequestForm()
    #if form.validate_on_submit():

    return render_template('traveler/traveler_dashboard.html')


# Traveler selecting a request on their dashboard, uses request_id to create page
@traveler.route("/traveler/request/<int:request_id>/")
def request():
    # SQLAlchemy to create page with request as well as itineraries created for request
    return render_template('')


# Traveler selecting itinerary on their request, use itinerary_id to create page
@traveler.route("/traveler/request/<int:request_id>/itinerary/<int:itinerary_id>")
def itinerary():
    # SQLAlchemy to create page with request and specific itinerary
    return render_template('')

# Traveler viewing history of requests
@traveler.route("/traveler/request/history/")
def requests_history():
    # SQLAlchemy to create page with current user's past requests
    return render_template('')