from django.contrib.auth import logout
from django.shortcuts import redirect

from cashborrower import settings


def ViewLogout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)