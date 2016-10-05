"""noortemaja URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from eventmanager import views
from django.conf.urls import include, url


admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^events/', views.EventList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/comments', views.CommentList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/likes', views.EventLikeList.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)/likes', views.CommentLikeList.as_view()),
    url(r'^gcm/(?P<registration_id>[0-9]+)/(?P<info>[0-9]+[a-z])', views.CommentLikeList.as_view()),
]
