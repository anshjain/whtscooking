# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from model_utils import Choices

#phone field application
from phonenumber_field.modelfields import PhoneNumberField


class Vendor(models.Model):
    """
    Vendor Model information
    """
    user = models.OneToOneField(User, editable=True)
    create_date = models.DateTimeField('Creation Date', auto_now_add=True)
    mobile_no = PhoneNumberField(null=True)

    def __unicode__(self):
        return "User %s from %s" %(self.user.first_name, self.mobile_no)

    def is_empty(self):
        return self.mobile_no is None


class HarmanLocation(models.Model):
    """
    Store office location, this will be used to identify menu specific location.
    """
    location = models.CharField(max_length=30, verbose_name="Office location")
    is_active = models.BooleanField(verbose_name="location active")

    def __unicode__(self):
        return u'{}'.format(self.location)


class MenuCard(TimeStampedModel):
    """
    Menu item entries for all at once.
    """
    item_name = models.CharField(max_length=30, verbose_name="Item Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    food_choice = Choices(('1', 'Veg'),
                          ('2', 'Non-Veg'))
    food_type = models.CharField(choices=food_choice,
                              max_length=10,
                              verbose_name='Food Type')

    def __unicode__(self):
        return u'{}-{}'.format(self.item_name, self.price)


class MenuType(TimeStampedModel):
    """
    Menu type is menu for breakfast, lunch, sneaks and dinner
    """
    type_name = models.CharField(max_length=30, verbose_name="Type Name")

    def __unicode__(self):
        return u'%s' % self.type_name


class VendorMenuType(TimeStampedModel):
    """
    Vendor and menu type relationship to verify which vendor allow for which type menu
    Based on this entries will allow to make entry in Vendor menu to vendor.
    and display as well.
    """
    vendor = models.ForeignKey(Vendor, verbose_name="Vendor")
    menu_type = models.ForeignKey(MenuType, verbose_name="Menu For")

    def __unicode__(self):
        return u'%s - %s' % (self.vendor_id, self.menu_type)


class VendorMenu(TimeStampedModel):
    """
    Vendor specific menu for the current day specific time
    Breakfast, lunch, sneak and dinner.
    """
    vendor = models.ForeignKey(Vendor, verbose_name="Vendor")
    menu = models.ForeignKey(MenuCard, verbose_name="Menu Name")
    menu_type = models.ForeignKey(MenuType, verbose_name="Menu For")
    location = models.ForeignKey(HarmanLocation, verbose_name="Menu For location")
    create_date = models.DateField('Creation Date', auto_now_add=True)

    class Meta:
        unique_together = ('menu', 'vendor', 'menu_type', 'create_date', 'location')


class UserRating(TimeStampedModel):
    md5 = models.CharField(max_length=50, verbose_name="md5", primary_key=True)
    vendor = models.ForeignKey(Vendor, verbose_name="Vendor", blank=True, null=True)
    rating_type = Choices(('2', 'Like'),
                          ('3', 'Super Like'),
                          ('1', 'Not Like'), )
    rating = models.CharField(choices=rating_type,
                              max_length=10,
                              verbose_name='Rating',
                              blank=True, null=True)
    why = models.CharField(max_length=255, blank=True, null=True)
    imp = models.CharField(max_length=255, blank=True, null=True)