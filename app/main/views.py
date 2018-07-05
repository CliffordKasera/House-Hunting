from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Listing,Timeslot,Image

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title)



@main.route('/single_listing/listing/<int:id>', methods = ['GET','POST'])
@login_required
def single_listing(id):

    '''
    view function that returns single listing page and its data
    '''
    form = BookingForm()
    single_listing = Listing.query.get(id = id)
    if form.validate_on_submit():
        # initializing instances
        
        
        email = form.email.data
        contact = form.contact.data
        name = form.name.data



        #listing instances
        new_single_listing = Listing(email = email, contact = contact, name = name)

        # save review 
        new_single_listing.save_listing()
        return redirect(url_for('.single_listing', id = new_single_listing.id ))

    title = f'{listing.title} listing'
    return render_template('single_listing.html', title = title, booking_form = boooking_form, booking_listing = booking_listing)


   

 