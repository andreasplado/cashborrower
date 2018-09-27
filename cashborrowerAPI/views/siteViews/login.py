from django.template.context_processors import csrf
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login

def view_login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


def view_auth_and_login(request, onsuccess='/', onfail='/login/'):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)


