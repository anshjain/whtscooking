from django.db import models


class Location(models.Model):
    """ model representing office locations """
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)


class Vendor(models.Model):
    """ model representing the vendors """
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)


class FoodItems(models.Model):
    """ model representing different food items """
    item = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=10, default='veg', choices=(('veg', 'Veg'), ('non-veg', 'Non Veg')))
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)


class Service(models.Model):
    """ model representing the type of services delivered by the vendor """
    name = models.CharField(max_length=10, default='lunch', choices=(('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('snacks', 'Snacks'), ('dinner', 'Dinner')))
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)


class VendorMenu(models.Model):
    """ model representing the vendors menu """
    vendor = models.ForeignKey(Vendor)
    service = models.ForeignKey(Service)
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def location(self):
        return self.vendor.location.name


class VendorMenuItems(models.Model):
    """ model representing different items in the vendors menu """
    vendor_menu = models.ForeignKey(VendorMenu)
    food_item = models.ForeignKey(FoodItems)
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def vendor(self):
        return self.vendor_menu.vendor.name

    @property
    def service(self):
        return self.vendor_menu.service.name

    @property
    def item(self):
        return self.food_item.name


class UserRating(models.Model):
    """ model representing user ratings """
    employee_id = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor)
    rating = models.IntegerField(choices=(('1', 'Bad'), ('2', 'Neutral'), ('3', 'Average'), ('4', 'Good')))
    comments = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    last_modified = models.DateTimeField(auto_now=True)
