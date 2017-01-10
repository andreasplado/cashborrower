from django.contrib.auth import logout
from django.shortcuts import redirect

from noortemaja import settings


def ViewLogout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)