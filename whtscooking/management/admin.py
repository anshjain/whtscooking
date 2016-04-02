from django.contrib import admin
from .models import Vendor, MenuCard, UserRating, MenuType, VendorMenuType, VendorMenu, HarmanLocation

# Register your models here.


class VendorAdmin(admin.ModelAdmin):

    model = Vendor
    list_display = ('mobile_no', 'user')


class MenuCardAdmin(admin.ModelAdmin):

    model = MenuCard
    list_display = ('item_name', 'price', 'description')


class MenuTypeAdmin(admin.ModelAdmin):

    model = MenuType
    list_display = ('type_name',)


class VendorMenuTypeAdmin(admin.ModelAdmin):

    model = VendorMenuType
    list_display = ('vendor', 'menu_type')


class UserRatingAdmin(admin.ModelAdmin):

    model = UserRating
    list_display = ('md5', 'vendor', 'rating')


class VendorMenuAdmin(admin.ModelAdmin):

    model = VendorMenu
    list_display = ('vendor', 'menu', 'menu_type', 'create_date')


class HarmanLocationAdmin(admin.ModelAdmin):

    model = HarmanLocation
    list_display = ('location', 'is_active')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(MenuCard, MenuCardAdmin)
admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(VendorMenuType, VendorMenuTypeAdmin)
admin.site.register(VendorMenu, VendorMenuAdmin)
admin.site.register(HarmanLocation, HarmanLocationAdmin)
