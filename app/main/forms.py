from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateField, TimeField, TextAreaField, MultipleFileField
from wtforms.validators import Required, Email
from ..models import User, Booking
from flask_wtf.file import FileField, FileAllowed
from wtforms import ValidationError


class ListingForm(FlaskForm):
    # image = MultipleFileField('Upload a few images',validators=[FileAllowed(['jpg', 'png']), Required()])
    one_image_path = MultipleFileField('Upload a few images',validators=[FileAllowed(['jpg', 'png']), Required()])
    location = SelectField('Neighbourhood', choices=[('eastleigh', 'Eastleigh'), ('karen', 'Karen'),
                                                     ('kileleshwa', 'Kileleshwa'), ('Langata', 'Langata'),
                                                     ('lavington', 'Lavington'), ('muthaiga', 'Muthaiga'),
                                                     ('ngara', 'Ngara'), ('runda', 'Runda'), ('donholm', 'Donholm'),
                                                     ('south-B', 'South-B'), ('south-C', 'South-C'),
                                                     ('upperhill', 'Upperhill'), ('westlands', 'Westlands')])
    category = SelectField('Type', validators=[Required()], choices=[('apartment', 'Apartment'),
                                                                    ('bungalow', 'Bungalow'),
                                                                    ('maisonette', 'Maisonette')])
    bedrooms = SelectField('Size', validators=[Required()], choices=[('bedsitter', 'Bedsitter'), ('1 Bedroom', '1 Bedroom'),
                                                                   ('2 Bedroom', '2 Bedroom'), ('3 Bedroom', '3 Bedroom'),
                                                                   ('4 Bedroom', '4 Bedroom')])
    pricing = IntegerField('Price', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')



class BookingForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    contact = StringField('Your Contact',validators =[Required()])
    name = StringField('Your name',validators =[Required()])
    submit = SubmitField('Sign In')


class TestForm(FlaskForm):
    submit = SubmitField('Submit')
    