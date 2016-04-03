"""whtscooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from management.views import home, UserRatings, vendor_menu, create_menu

urlpatterns = [	
    url(r'^$', home, name='static-home'),
    url(r'^vendors/$', vendor_menu, name='vendor-home'),
    url(r'^vendors/create/$', create_menu, name='vendor-create'),
    url(r'^rating/$', UserRatings.as_view(), name='rating-home'),
    url(r'^harman-admin/', include(admin.site.urls)),
]