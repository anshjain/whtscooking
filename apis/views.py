from datetime import date
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import OrderedDict

from models import Location, Vendor, VendorMenu, VendorMenuItems


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
            food_items[menu.service.name] = self.get_food_items(vendor, menu.service)
        return food_items

    def get_food_items(self, vendor, service):
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

    def get_context_data(self, **kwargs):
        context_data = super(VendorView, self).get_context_data(**kwargs)
        context_data['timings'] = ['Breakfast', 'Lunch', 'Snacks', 'Dinner']
        context_data['user_type'] = 'vdor'
        return context_data