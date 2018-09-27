from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request
from django.shortcuts import render_to_response, redirect, render
from django.template.context_processors import csrf
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from cashborrowerAPI.models.tokens import account_activation_token


def view_register(request):
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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

def account_activation_sent():
    render_to_response('templates/account_activation_sent.html')