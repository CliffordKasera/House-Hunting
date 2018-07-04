from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField, SelectField, IntegerField, DateField, TimeField, TextAreaField
from wtforms.validators import Required
from ..models import User
from wtforms import ValidationError


class ListingForm(FlaskForm):
    images = MultipleFileField('Upload a few images',validators=[FileAllowed(['jpg', 'png']), Required])
    location = SelectField('Neighbourhood', choices=[('eastleigh', 'Eastleigh'), ('karen', 'Karen'),
                                                     ('kileleshwa', 'Kileleshwa'), ('Langata', 'Langata'),
                                                     ('lavington', 'Lavington'), ('muthaiga', 'Muthaiga'),
                                                     ('ngara', 'Ngara'), ('runda', 'Runda'),
                                                     ('south-B', 'South-B'), ('south-C', 'South-C'),
                                                     ('upperhill', 'Upperhill'), ('westlands', 'Westlands')])
    category = SelectField('Type', validators=[Required], choices=[('apartment', 'Apartment'),
                                                                    ('bungalow', 'Bungalow'),
                                                                    ('maisonette', 'Maisonette')])
    bedrooms = SelectField('Size', validators=[Required], choices=[('bedsitter', 'Bedsitter'), ('1 Bedroom', '1 Bedroom'),
                                                                   ('2 Bedroom', '2 Bedroom'), ('3 Bedroom', '3 Bedroom'),
                                                                   ('4 Bedroom', '4 Bedroom')])
    pricing = IntegerField('Price', validators=[Required])
    description = TextAreaField('Description', validators=[Required])
    view_date = DateField('Date', validators=[Required])
    view_start_time = TimeField('From', min="9:00", max="18:00", validators=[Required])
    view_end_time = TimeField('To', validators=[Required])
    submit = SubmitField('Submit')
