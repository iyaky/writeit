from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def badges(request):
    return render(request, 'badges/badges.html')
