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
from eventmanager.views import(
   LoanDeleteAPIView,
   LoanDetailAPIView,
   LoanListView,
   LoanUpdateAPIView ,
)


admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^loans/$', views.LoanListView.as_view()),
    url(r'^loan/(?P<id>[0-9]+)', views.LoanDetailAPIView.as_view()),
    url(r'^loan/update/(?P<id>[0-9]+)/', views.LoanUpdateAPIView.as_view()),
    url(r'^loan/delete/(?P<id>[0-9]+)', views.LoanDeleteAPIView.as_view()),

    url(r'^loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    url(r'^loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    url(r'^loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    url(r'^loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]
