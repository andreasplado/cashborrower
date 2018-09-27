from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required(login_url='/login/')
def secured(request):
    return render_to_response("../templates/dashboard.html")