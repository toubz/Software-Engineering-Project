from flask import Blueprint, Flask, render_template, request, redirect, url_for
from .forms import CreateItineraryForm


local = Blueprint('local', __name__, template_folder='templates')

# Brings local to their homepage
@local.route("/local/dashboard/")
def local_dashboard():
    # Need to send requests to dashboard
    # Query for requests, need to base them based on location and status
    requests = Request.query.filter()


    return render_template(
        'local/local_dashboard.html',
        requests=requests)


# Local selecting a request from their dashboard, uses request_id to create page
@local.route("/local/request/<int:request_id>/")
def request():
    # Filter for selected request to display
    request = Request.query.filter()

    return render_template(
        'local/view_request.html',
        request=request)


# Local create itinerary page, uses request_id to to create page
@local.route("/local/request/<int:request_id>/itinerary/")
def create_itinerary():
    form = CreateItineraryForm()

    return render_template(
        'local/create_itinerary.html',
        form=form)


# Local viewing itineraries created on account
@local.route("/local/itinerary/history/")
def itinerary_history():
    # SQLAlchemy to create page of created itineraries associated with current user's user_id
    itineraries = Itinerary.query.filter()

    return render_template(
        'local/itiinerary_history.html',
        itineraries=itineraries)


# Local viewing a single itinerary that was created
@local.route("/local/itinerary/<int:itinerary_id>/")
def itinerary():
    # SQLAlchemy to create page of selected itinerary using itinerary_id
    itinerary = Itinerary.query.filter()

    return render_template(
        'local/view_itinerary.html',
        itinerary=itinerary)
