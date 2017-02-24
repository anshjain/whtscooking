from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ home page """
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context_data = super(HomeView, self).get_context_data(**kwargs)
        context_data['vendors'] = ['anna', 'sahyadri']
        context_data['timings'] = ['Breakfast', 'Lunch', 'Evening-snacks', 'Dinner']
        context_data['food_types'] = ['veg', 'non-veg']
        context_data['user_type'] = 'vdor'  # need to get it from user object
        return context_data


class VendorView(TemplateView):
    """ Vendor home page """
    template_name = "vendor-home.html"

    def get_context_data(self, **kwargs):
        context_data = super(VendorView, self).get_context_data(**kwargs)
        context_data['timings'] = ['Breakfast', 'Lunch', 'Snacks', 'Dinner']
        context_data['user_type'] = 'vdor'
        return context_data