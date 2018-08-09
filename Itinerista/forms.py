from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField, IntegerField, StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length


# User signup
class SignUpForm(FlaskForm):
    user_id = HiddenField()
    first_name = StringField(
        'First Name',
        validators = [InputRequired(), Length(max=50, message="Cannot be longer than 50 characters")],
        render_kw={'placeholder': "What's your first name?",
                   'maxlength': '50'})
    last_name = StringField(
        'Last Name',
        validators = [InputRequired(), Length(max=50, message="Cannot be longer than 50 characters")],
        render_kw={'placeholder': "What's your last name?",
                   'maxlength': '50'})
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': "Create a password",
                   'maxlength': '50'})
    email_address = StringField(
        'Email Address',
        validators = [InputRequired(), Length(max=50, message="Cannot be longer than 50 characters")],
        render_kw={'placeholder': "What's your email?",
                   'maxlength': '50'})
    phone_number = IntegerField(
        'Phone Number',
        validators = [InputRequired(), Length(max=20, message="Cannot be longer than 20 characters")],
        render_kw={'placeholder': "What's your phone nunber?",
                   'maxlength': '20'})

    traveler_submit = SubmitField()
    local_submit = SubmitField()

    # Validators for account info
    def validate(self):
        result = super().validate()

        # Add some other validators we'll need for users besides the ones I have


# Request form that will have all fields of a request
class CreateRequestForm(FlaskForm):
    request_name = StringField(
        'Request Plans Name',
        validators = [InputRequired(), Length(max=25, message="Cannot be longer than 20 characters")],
        render_kw={'placeholder': "Create a name for this request",
                   'maxlength': '25'})
    start_date = DateField(
        'Start Date',
        validators = [InputRequired()])
    end_date = DateField(
        'End Date',
        validators = [InputRequired()])
    location = StringField(
        'Travel Location')
    total_budget = IntegerField(
        'Estimated Budget',
        validators = [InputRequired(), Length(max=10, message="Cannot be longer than 10 characters")],
        render_kw={'placeholder': "This number will be used when locals created itineraries for you",
                   'maxlength': '10'})
    interests = StringField(
        'Interests',
        validators = [InputRequired(), Length(max=250, message="Cannot be longer than 250 characters")],
        render_kw={'placeholder': "Give locals an idea of some of your interests. What do you enjoy doing? Anything you want to do/see in particular?",
                   'maxlength': '250'})
    additional_comments = StringField(
        'Additional Comments',
        validators = [InputRequired(), Length(max=250, message="Cannot be longer than 250 characters")],
        render_kw={'placeholder': "Anything else you'd like locals to know?",
                   'maxlength': '250'})

    # Validators for request info
    def validate(self):
        result = super().validate()

        # Add some other validators we'll need for requests besides the ones I have


# Itinerary form with all required fields of an itinerary 
class CreateItineraryForm():
    local_id = HiddenField()
    request_id = HiddenField()
    itinerary_id = HiddenField()

    itinerary_name = StringField(
        'Itinerary Name',
        validators = [InputRequired(), Length(max=25, message="Cannot be longer than 20 characters")],
        render_kw={'placeholder': "Create a name for this itinerary",
                   'maxlength': '25'})
    activities = []

    # Validators for itinerary info
    def validate(self):
        result = super().validate()

        # Add some other validators we'll need for itineraries besides the ones I have


# Activity class with all required fields of an activity
class Activity(FlaskForm):
    activity_date = HiddenField()
    activity_name = StringField(
        'Activity Name',
        validators = [InputRequired(), Length(max=25, message="Cannot be longer than 20 characters")],
        render_kw={'placeholder': "Create a name for this activity",
                   'maxlength': '25'})
    start_time = DateField(
        'Start Time',
        validators = [InputRequired()])
    end_time = DateField(
        'End Time',
        validators = [InputRequired()])
    activity_location = StringField(
        'Location')
    min_price = IntegerField(
        'Minimum Price',
        validators = [InputRequired(), Length(max=10, message="Cannot be longer than 10 characters")],
        render_kw={'placeholder': "Min",
                   'maxlength': '10'})
    max_price = IntegerField(
        'Maximum Price',
        validators = [InputRequired(), Length(max=10, message="Cannot be longer than 10 characters")],
        render_kw={'placeholder': "Max",
                   'maxlength': '10'})
    description = StringField(
        'Description',
        validators = [InputRequired(), Length(max=250, message="Cannot be longer than 250 characters")],
        render_kw={'placeholder': "Please describe what this activity is and what the traveler has to look forward to.",
                   'maxlength': '250'})

    # Validators for activity info
    def validate(self):
        result = super().validate()

        # Add some other validators we'll need for activites besides the ones I have

            # Need activity date validation, has to be within request date range 