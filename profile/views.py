"""
-- whats cooking harman internal project
"""
from collections import OrderedDict
from datetime import date

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import FormView, TemplateView

from apis.models import Location, Vendor, VendorMenu, VendorMenuItems, FoodItems, Service
from forms import LoginForm, EMP_USER, VDOR_USER


class LoginView(FormView):
    """ login page """
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # TODO: set user type in request session.
            return HttpResponseRedirect(reverse('home'))
        return super(LoginView, self).get(self, request, *args, **kwargs)

    def form_valid(self, form):
        """ save the user type in session and redirect to home page """
        user_type = form.cleaned_data.get('user_type')
        message = 'Invalid login'

        # if user employee type do ldap verification and login.
        if user_type == EMP_USER:
            # do ldap coding here !
            user = None
            message = "LDAP authenticate is not implemented yet!!"
        else:
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

            if user is not None:
                login(self.request, user)
                return HttpResponseRedirect(reverse('vendor-home'))
        form.errors.update({'username': message})
        # TODO: set user type in request session.
        return render_to_response(self.template_name, context_instance=RequestContext(self.request, {'form': form}))


def logout_view(request):
    """ logout page """
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class HomeView(TemplateView):
    """ home page """
    template_name = "home.html"

    def get_locations(self):
        """
        get all locations
        :return:
        """
        return Location.objects.all()

    def get_vendors(self, location_ids):
        """
        :param location_ids:
        :return:
        """
        return Vendor.objects.filter(location__in=[location_ids]).order_by('-created_at')

    def get_service_list(self, vendor, location_ids):
        """
        Get VendorMenu list
        :return:
        """
        menus = VendorMenu.objects.filter(location__in=[location_ids], vendor=vendor).order_by('created_at')
        food_items = OrderedDict()
        for menu in menus:
            food_items[menu.service.name] = self.get_vendor_menu_items(vendor, menu.service)
        return food_items

    def get_vendor_menu_items(self, vendor, service):
        """
        Get VendorMenuItems list
        :return:
        """
        items = {'veg': [], 'non-veg': []}
        food_items = VendorMenuItems.objects.filter(vendor_menu__vendor=vendor,
                                                    vendor_menu__service=service,
                                                    created_at=date.today())
        for item in food_items:
            if item.food_item.type == 'veg':
                items[item.food_item.type].append(item)
            else:
                items[item.food_item.type].append(item)
        return items

    def get_context_data(self, **kwargs):
        """
        Context data
        :param kwargs:
        :return:
        """
        context_data = super(HomeView, self).get_context_data(**kwargs)

        locations = self.get_locations()
        vendors = self.get_vendors(locations[0].id)

        vendor_dict = OrderedDict()
        for vendor in vendors:
            vendor_dict[vendor.name] = self.get_service_list(vendor, locations[0].id)
        context_data.update({'locations': locations, 'vendors': vendor_dict,
                             'food_types': ['veg', 'non-veg']})

        context_data['user_type'] = 'vdor'  # need to get it from user object
        return context_data


class VendorView(LoginRequiredMixin, TemplateView):
    """ Vendor home page """
    template_name = "vendor-home.html"

    def get_food_items(self, service):
        """
        Get VendorMenuItems list
        :return:
        """
        return FoodItems.objects.filter(service=service)

    def get_services(self):
        """
        Get VendorMenuItems list
        :return:
        """
        services = Service.objects.all().order_by("created_at")
        items = OrderedDict()
        for service in services:
            items[service] = self.get_food_items(service)
        return items

    def get_context_data(self, **kwargs):
        context_data = super(VendorView, self).get_context_data(**kwargs)
        context_data['services'] = self.get_services()
        context_data['user_type'] = 'vdor'
        return context_data