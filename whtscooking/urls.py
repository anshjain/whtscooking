from django.conf.urls import include, url
from django.contrib import admin

from profile.views import LoginView, logout_view
from apis.views import HomeView

urlpatterns = [
    # normal views
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', logout_view, name='logout'),

    # Admin views
    url(r'^admin/', include(admin.site.urls)),
]
