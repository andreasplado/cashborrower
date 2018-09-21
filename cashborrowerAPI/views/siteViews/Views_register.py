from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


def ViewRegister(request, onsuccess='/', onfail='/login/'):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return HttpResponseRedirect('/accounts/register/complete')
        else:
            form = UserCreationForm()
            token = {}
            token.update(csrf(request))
            token['form'] = form

            return render_to_response('registration/registration_form.html', token)

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def registration_complete(request):
    return render_to_response('templates/user_created_successfully.html')