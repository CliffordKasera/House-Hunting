from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, MultipleFileField, SelectField, IntegerField, DateField, TimeField, TextAreaField, StringField
from wtforms.validators import DataRequired
from ..models import User
from wtforms import StringField, SubmitField, MultipleFileField, SelectField, IntegerField, DateField, TimeField, TextAreaField
from wtforms.validators import Required
from ..models import User, Booking
from wtforms import ValidationError


class ListingForm(FlaskForm):
    images = MultipleFileField('Upload a few images', validators=[FileAllowed(['jpg', 'png']), DataRequired()])
    location = SelectField('Neighbourhood', choices=[('eastleigh', 'Eastleigh'), ('karen', 'Karen'),
                                                     ('kileleshwa', 'Kileleshwa'), ('Langata', 'Langata'),
                                                     ('lavington', 'Lavington'), ('muthaiga', 'Muthaiga'),
                                                     ('ngara', 'Ngara'), ('runda', 'Runda'), ('donholm', 'Donholm'),
                                                     ('south-B', 'South-B'), ('south-C', 'South-C'),
                                                     ('upperhill', 'Upperhill'), ('westlands', 'Westlands')])
    category = SelectField('Type', validators=[DataRequired()], choices=[('apartment', 'Apartment'),
                                                                    ('bungalow', 'Bungalow'),
                                                                    ('maisonette', 'Maisonette')])
    bedrooms = SelectField('Size', validators=[DataRequired()], choices=[('bedsitter', 'Bedsitter'), ('1 Bedroom', '1 Bedroom'),
                                                                   ('2 Bedroom', '2 Bedroom'), ('3 Bedroom', '3 Bedroom'),
                                                                   ('4 Bedroom', '4 Bedroom')])
    pricing = IntegerField('Price', format="%d/%m/%Y", validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    view_date = DateField('Date', validators=[DataRequired()])
    view_start_time = TimeField('From', validators=[DataRequired()])
    view_end_time = TimeField('To', validators=[DataRequired()])
    submit = SubmitField('Submit')


class BookingForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    contact = ContactField('Your Contact',validators =[Required()])
    name = NameField('Your name'),validators =[Required()])
    submit = SubmitField('Sign In')