from django.shortcuts import redirect

from cashborrowerAPI.views.siteViews.login import view_auth_and_login
from cashborrowerAPI.views.siteViews.register import user_exists, create_user


def sign_up(request, onsuccess='/', onfail='/login/'):
    username = request.POST.get("username", None);
    email = request.POST.get("email", None)
    password = request.POST.get("password", None);
    if not user_exists(username):
        create_user(username=username, email=email, password=password)
        return redirect("/")
    else:
        return redirect("/login/")