from flask import Blueprint, Flask, render_template, request, redirect, url_for

local = Blueprint('local', __name__, template_folder='templates')

# Brings local to their homepage
@local.route("/local/dashboard/")
def local_dashboard():
    return render_template('local/local_dashboard.html')


# Local selecting a request from their dashboard, uses request_id to create page
@local.route("/local/request/<int:request_id>/")
def request():
    return render_template('')


# Local create itinerary page, uses request_id to to create page
@local.route("/local/request/<int:request_id>/itinerary/")
def create_itinerary():
    return render_template('')


# Local viewing itineraries created on account
@local.route("/local/itinerary/history/")
def itinerary_history():
    # SQLAlchemy to create page of created itineraries associated with current user's user_id
    return render_template('')


# Local viewing a single itinerary that was created
@local.route("/local/itinerary/<int:itinerary_id>/")
def itinerary():
    # SQLAlchemy to create page of selected itinerary using itinerary_id
    return render_template('')