from django.conf.urls import url

from cashborrowerAPI.views.siteViews import Views_register
from cashborrowerAPI.views.siteViews.Views_register import registration_complete

urlpatterns = [
    # Registration URLs
    url(r'^accounts/register/$', Views_register),
    url(r'^accounts/register/complete/$', registration_complete),
]