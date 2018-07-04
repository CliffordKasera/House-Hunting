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
    form = ListingForm()
    single_listing = Listing.query.get(id = id)
    if form.validate_on_submit():
        # initializing instances
        # single_listing = form.single_listing.data
        location = form.location.data
        description = form.description.data
        category = form.category.data
        bedrooms = form.bedrooms.data
        lister_id = form.lister_id.data
        pricing = form.pricing.data
        image = form.image.data
        timeslot =form.timeslot.data



        #listing instance
        new_single_listing = Listing(location = location, description = description, category = category,  bedrooms =  bedrooms,  pricing =  pricing, lister_id = current_user.id, image = image, timeslot = timeslot)

        # save review 
        new_single_listing.save_listing()
        return redirect(url_for('.single_listing', id = new_single_listing.id ))

    title = f'{listing.title} listing'
    return render_template('form_listing.html', title = title, listing_form = form, single_listing = single_listing)


   

 