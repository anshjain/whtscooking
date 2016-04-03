# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from django import forms
from .models import UserRating, MenuCard, VendorMenu, MenuType, HarmanLocation, Vendor


class FormUserRatings(forms.Form):
    vchoices = [(obj.id, obj.user.first_name) for obj in Vendor.objects.filter(user__is_active=True)]
    vendor = forms.ChoiceField(widget=forms.RadioSelect, choices=vchoices)
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=UserRating.rating_type)


class VendorMenuForm(forms.Form):
    """
    This form is for vendor to make everyday entries for food item for breakfast, lunch, sneaks and dinner
    """
    mchoices = [(obj.id, obj.type_name) for obj in MenuType.objects.all()]
    vchoices = [(obj.id, obj.item_name) for obj in MenuCard.objects.all()]

    vendor = forms.HiddenInput()
    location = forms.HiddenInput()
    menu_type = forms.ChoiceField(choices=mchoices, widget=forms.RadioSelect(), label='Menu Type')
    menu = forms.ChoiceField(choices=vchoices, label='Menu Item', widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = VendorMenu
        fields = ('vendor', 'location', 'menu_type', 'menu')


class LocationForm(forms.Form):
    """
    Form to lock user location and based on which will identify food menu and rating to the vendor.
    """
    lochoices = [('--', 'select')] + [(obj.id, obj.location) for obj in HarmanLocation.objects.all()]
    location = forms.ChoiceField(choices=lochoices, label="office location",
                                 widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    class Meta:
        model = HarmanLocation
        fields = ('location', )