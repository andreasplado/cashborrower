from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from domain import settings


def ViewLogout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)