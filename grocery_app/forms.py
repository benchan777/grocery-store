from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryItem, GroceryStore, ItemCategory, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Name', validators=[DataRequired(), Length(min = 3, max = 80)])
    address = StringField('Store Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Item Name', validators=[DataRequired()])
    price = FloatField('Item Price')
    category = SelectField('Category', choices=[('DELI', 'Deli'), ('BAKERY', 'Bakery'), ('PANTRY', 'Pantry'), ('FROZEN', 'Frozen'), ('OTHER', 'Other')])
    photo_url = StringField('Photo Url', validators=[DataRequired(), URL()])
    store = QuerySelectField('Store Name', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    """ Form for new user sign up """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """ Form for logging in """
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')