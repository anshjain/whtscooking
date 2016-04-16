# -*- coding: utf-8 -*-

import copy
import datetime
import hashlib

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic.edit import FormView


from .contants import LOCATION_COOKIES, DATE_STRING
from .forms import FormUserRatings, LocationForm, VendorMenuForm
from .models import UserRating, Vendor, VendorMenu, MenuCard, MenuType, HarmanLocation


def set_cookie(response, key, value, days_expire=7):
    """
    Method to set cookies
    :param response:
    :param key:
    :param value:
    :param days_expire:
    :return:
    """
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60

    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         DATE_STRING)

    response.set_cookie(key, value, max_age=max_age, expires=expires,
                        domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)
    return response


def home(request):
    """
    Default welcome page on harman food court, with location form
    """
    template = "index.html"
    form_class = LocationForm()
    context = {}
    loc_name = ''

    if request.method == 'POST':
        loc_name = request.POST.get('location')
    elif request.COOKIES.get(LOCATION_COOKIES):
        loc_name = request.COOKIES.get(LOCATION_COOKIES)
    else:
        context.update({'form': form_class})


    response = render_to_response(template, context,
                                  context_instance=RequestContext(request))

    return set_cookie(response, LOCATION_COOKIES, loc_name)


def vendor_menu(request):
    """
    Method to display all vendor menu items on page with current date on top of the page.
    :param request:
    :return:
    """
    template = 'user_dashboard.html'
    current_date = datetime.datetime.now()
    vendor_menus = []
    loc_name = request.COOKIES.get(LOCATION_COOKIES)

    if not loc_name:
        return redirect(reverse('static-home'))

    vendors = Vendor.objects.filter(user__is_active=True)
    locations = HarmanLocation.objects.filter(is_active=True)

    for vendor in vendors:
        menu_item = VendorMenu.objects.\
            filter(create_date=current_date).filter(location=loc_name).\
            filter(vendor=vendor).values('menu_type__type_name', 'menu__food_type', 'menu__item_name',
                                         'menu__price', 'menu__description')

        vendor_menus.append((vendor.user.first_name, menu_item))

    context = {'vendor_menus': vendor_menus, 'current_date': current_date,
               'vendors': vendors, 'locations': locations}
    return render_to_response(template, context,
                              context_instance=RequestContext(request))


#@login_required()
def create_menu(request):
    """
    Vendor will create menu for the current date
    :param request:
    :return:
    """
    loc_code = request.COOKIES.get(LOCATION_COOKIES)
    vendor_code = 1  # should appear from logged in user only.
    form_class = VendorMenuForm(request.POST or None,
                                initial={"vendor": vendor_code, "location": loc_code})
    template_name = "vendor_menu.html"

    if not loc_code:
        return redirect(reverse('static-home'))

    if request.method == 'POST':
        vendor = Vendor.objects.filter(id=vendor_code).first()
        menu_type = MenuType.objects.filter(id=form_class.data.get('menu_type')).first()
        loc_code = HarmanLocation.objects.get(id=loc_code)
        menu_items = []
        for item in form_class.data.getlist('menu'):
            item_obj = MenuCard.objects.filter(id=item).first()
            menu_items.append(VendorMenu(menu=item_obj, menu_type=menu_type,
                                         location=loc_code, vendor=vendor))

        VendorMenu.objects.bulk_create(menu_items)
        form_class.errors['menu'] = []

    context = {'form': form_class}
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


class UserRatings(FormView):
    template_name = "user_rating.html"
    form_class = FormUserRatings
    success_url = '/rating/'

    def _save_info(self):
        vendor_id = self.request.POST['vendor']
        rating_id = self.request.POST['rating']
        user_agent = self.request.META['HTTP_USER_AGENT']
        current_time = datetime.datetime.utcnow().time()
        if current_time > settings.RATING_TIME:
            status = 2
            message = "Rating can't be done before {} PM".format(settings.RATING_TIME)
            return {'status': status, 'message': message}

        user_hash = hashlib.sha1(str(datetime.date.today()) + user_agent).hexdigest()
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            user_rate, created = UserRating.objects.get_or_create(
                md5=user_hash)

            user_rate.rating = rating_id
            user_rate.vendor_id = vendor

            if created:
                status = 2
                message = 'Thanks For the update your rating, Its saved in our Database successfully'
            else:
                user_rate.why = self.request.POST.get('why', '')
                user_rate.imp = self.request.POST.get('imp', '')
                status = 1
                message = 'Thanks For the rating, Its saved in our Database successfully'
            user_rate.save()
        except:
            status = 2
            message = 'System Error! Unable to save response.'

        return {'status': status, 'message': message}

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        data = self._save_info()
        self.request.session['data'] = data
        return super(UserRatings, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserRatings, self).get_context_data(**kwargs)
        user_rating_dict = self._process_user_rating()
        context.update(self.request.session.pop('data', {}))
        context['user_rating_dict'] = user_rating_dict
        return context

    def _process_user_rating(self):
        """
        Process User Rating
        :return: user_rating_dict
        """
        user_rating_dict = {}
        user_rating_inner_dict = {'rating_super_like': 0,
                                  'rating_like': 0,
                                  'rating_not_like': 0}
        for vendor in Vendor.objects.all():
            user_rating_dict.update({vendor.user.first_name: copy.copy(user_rating_inner_dict)})

        for vendor in Vendor.objects.all():
            for user_rating in UserRating.objects.all():
                if user_rating.rating == '1' and vendor == user_rating.vendor:
                    user_rating_dict[vendor.user.first_name]['rating_super_like'] += 1
                elif user_rating.rating == '2' and vendor == user_rating.vendor:
                    user_rating_dict[vendor.user.first_name]['rating_like'] += 1
                elif user_rating.rating == '3' and vendor == user_rating.vendor:
                    user_rating_dict[vendor.user.first_name]['rating_not_like'] += 1

        return user_rating_dict
