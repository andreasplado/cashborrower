from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.template import loader
from django.template.context_processors import csrf

from cashborrowerAPI.models.models import Loan, User

@login_required(login_url='/login/')
def ViewIndex(View):
    loans = Loan.objects.order_by('-id')
    context = {
        'loans': loans
    }
    return render_to_response('../templates/dashboard.html', context)