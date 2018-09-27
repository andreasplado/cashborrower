from django.shortcuts import render_to_response


def ViewLoginRequired(View):
    return render_to_response('../templates/login_required.html')