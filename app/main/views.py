from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Listing, User, Image, Timeslot, Booking
from .forms import ListingForm, BookingForm
from flask_login import login_required, current_user
# Views
@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View home function that returns the home page
    '''
    apartment =  Listing.query.filter_by(category = 'apartment').all()
    bungalow = Listing.query.filter_by(category="bungalow").all()
    maisonette = Listing.query.filter_by(category="maisonete")
    listing = Listing.query.filter_by().all()

    title = 'Home | Boma Listing'
    return render_template('index.html', title = title, apartment = apartment, bungalow = bungalow, maisonette = maisonette, listing = listing)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    '''
    View profile page function that returns the profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    title = f"{uname.capitalize()}'s Profile"

    get_all_listings = Listing.query.filter_by(lister_id= User.id).all()

    if user is None:
        abort (404)

    return render_template("profile/profile.html", user = user, title=title, listings = get_all_listings)

@main.route('/listing/new',methods = ['GET','POST'])
@login_required
def listing():
    '''
    View listing function that returns the listing page and data
    '''
    list_form = ListingForm()

    # if list_form.validate_on_submit():
    #
    #     new_listing = Listing( location=list_form.location.data, category = list_form.category.data, pricing = list_form.pricing.data, bedrooms = list_form.bedrooms.data, user = current_user)
    #     new_listing.save_listing()
    #     new_timeslot = Timeslot (date = list_form.date.data, start_time = list_form.view_start_time.data, end_time = list_form.view_end_time.data,listing_id=listing.id)
    #
    #     for image in list_form.image.data:
    #     #     new_image = Im
    #     #
    #     # filename = photos.save(request.files['photo'])
    #     # path = f'photos/{filename}'
    #     # user.profile_pic_path = path
    #     # db.session.commit()
    #
    #
    #     return redirect(url_for('.index'))


    title = 'New Listing'
    return render_template('listing.html', list_form = list_form)


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

@main.route('/user/profile/booking/',methods = ['GET', 'POST'])
def booking():
    '''
    View booking function that returns the booking page and data
    '''
    get_all_bookings = Timeslot.query.filter_by(listing = listing.id).all()
    # booking_form = BookingForm()

    # if booking_form.validate_on_submit():
    #     new_booking = Booking(email=booking_form.email.data, name=booking_form.name.data, contact = booking_form.contact.data)
    #     new_booking.save_booking()


    return render_template('booking.html', booking = get_all_bookings)
