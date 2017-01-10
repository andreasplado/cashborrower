"""cashborrower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from cashborrowerAPI.views.siteViews.Views_index import ViewIndex
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
from cashborrowerAPI.views.siteViews.Views_login_required import ViewLoginRequired

from cashborrowerAPI.views.siteViews.Views_register import ViewRegister
from cashborrowerAPI.views.siteViews.Views_login import auth_and_login, loginview
from cashborrowerAPI.views.siteViews.Views_logout import ViewLogout

admin.autodiscover()
urlpatterns = [

    # ADMIN #
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^cashorrower-api/', include('cashborrowerAPI.urls')),

    url(r'^$', ViewIndex), #secured
    url(r'^dashboard/$', ViewIndex),

    url(r'^login/', loginview),
    url(r'^auth/', auth_and_login),
    url(r'^signup/', ViewRegister),
    url(r'^logout/', ViewLogout),

]