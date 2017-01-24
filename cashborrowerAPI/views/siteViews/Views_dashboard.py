from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from cashborrowerAPI.models.models import Loan



'''@login_required
def ViewDashboard(request):
    loans = Loan.objects.order_by('-id')
    context = {
        'loans': loans
    }

    #if request.user.is_authenticated():
    return render_to_response('../templates/dashboard.html', context)
    #else:
        #return render_to_response('../templates/login_required.html', context)
        '''

@login_required(login_url='/login/')
def secured(request):
    return render_to_response("../templates/dashboard.html")