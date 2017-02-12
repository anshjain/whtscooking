from django.conf.urls import include, url
from django.contrib import admin

from profile import views

urlpatterns = [
    # normal views
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.logout_view, name='logout'),

    # Admin views
    url(r'^admin/', include(admin.site.urls)),
]
