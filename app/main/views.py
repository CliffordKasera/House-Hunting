from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Listing, User, Image, Timeslot
from .forms import ListingForm
# Views
@main.route('/', methods = ['GET', 'POST'])
def home():
    '''
    View home function that returns the home page
    '''
    Apartment = Listing.query.filter_by(category="Apartment").all()
    Bungalow = Listing.query.filter_by(category="Bungalow").all()
    Maisonete = Listing.query.filter_by(category="Maisonete").all()
    listing = Listing.query.filter_by(lister_id).first()

    title = 'Home | Boma Listing'
    return render_template('index.html', title = title, Apartment = Apartment, Bungalow = Bungalow, Maisonette = Maisonette, listing = listing)
   

@main.route('/user/<uname>')
def profile(uname):
    '''
    View profile page function that returns the profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    title = f"{uname.capitalize()}'s Profile"

    get_all_listings = Listing.query.filter_by(agent = User.id).all()

    if user is None:
        abort (404)

    return render_template("profile/profile.html", user = user, title=title, listings = get_all_listings)

@main.route('/listing/new',methods = ['GET','POST'])
def listing():
    '''
    View listing function that returns the listing page and data
    '''
    list_form = ListingForm()

    if list_form.validate_on_submit():
        images = list_form.images.data
        location = list_form.location.data
        category = list_form.category.data
        bedrooms = list_form.bedrooms.data
        pricing = list_form.pricing.data
        timeSlotDate = list_form.time-slot-date.data

        new_listing = Pitch(images=images, location=location, category = category, pricing = pricing, bedrooms = bedrooms, time = timeSlotDate  user = current_user)
        new_listing.save_listing()

        return redirect(url_for('.singlelisting'))


    title = 'New Listing'
    return render_template('listing.html', listing_form = list_form)
    

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    '''
    View update profile page function that returns the update profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


