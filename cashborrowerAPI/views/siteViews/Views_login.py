from django.template.context_processors import csrf
from pip import logger

from cashborrowerAPI.views.siteViews.Views_register import user_exists, create_user
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


def auth_and_login(request, onsuccess='/', onfail='/login/'):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    #print(' username: ' + username +' password: ' + password + 'request: '+ request)
    print(request.POST.get('username', ''))
    print(request.POST.get('password', ''))
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return auth_and_login(request)
    else:
        return redirect("/")


