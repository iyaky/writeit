from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def challenges(request):
    return render(request, 'challenges/challenges.html')

@login_required
def new_challenge(request):
    return render(request, 'challenges/new_challenge.html')
