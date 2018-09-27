from django.conf.urls import url

from cashborrowerAPI.views.siteViews import register
from cashborrowerAPI.views.siteViews.register import registration_complete

urlpatterns = [
    # Registration URLs
    url(r'^accounts/register/$', register),
    url(r'^accounts/register/complete/$', registration_complete),
]