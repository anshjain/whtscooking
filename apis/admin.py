from django.contrib import admin

from . import models

# for HRs
admin.site.register(models.Location)
admin.site.register(models.Vendor)
admin.site.register(models.FoodItems)

# for vendors
admin.site.register(models.Service)
admin.site.register(models.VendorMenu)
admin.site.register(models.VendorMenuItems)




