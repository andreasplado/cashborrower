from django.contrib.auth import logout
from django.shortcuts import redirect

from cashborrower import settings


def logout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)