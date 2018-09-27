from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from cashborrowerAPI.models.models import Loan


@login_required(login_url='/login/')
def ViewIndex(View):
    loans = Loan.objects.order_by('-id')
    context = {
        'loans': loans
    }
    return render_to_response('../templates/dashboard.html', context)