# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from django import forms
from .models import UserRating, MenuCard, VendorMenu, MenuType


class FormUserRatings(forms.Form):
    vendor = forms.ChoiceField(widget=forms.RadioSelect, choices=[])
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=UserRating.rating_type)


class VendorMenuForm(forms.Form):
    """
    This form is for vendor to make everyday entries for food item for  breakfast, lunch, sneaks and dinner
    """
    mchoices = [ (obj.id, obj.type_name) for obj in MenuType.objects.all()]
    vchoices = [ (obj.id, obj.item_name) for obj in MenuCard.objects.all()]

    vendor = forms.HiddenInput()
    menu_type = forms.ChoiceField(choices=mchoices, widget=forms.RadioSelect(), label=('Menu Type'))
    menu = forms.ChoiceField(choices=vchoices, label=('Menu Item'), widget = forms.CheckboxSelectMultiple())

    class Meta:
        model = VendorMenu
        fields = ('menu_type', 'menu')