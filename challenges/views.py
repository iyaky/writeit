from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import NewChallengeForm
from challenges.models import Challenge
from django.db.models import F

@login_required
def challenges(request):
    challenges = Challenge.objects.exclude(challenge_starter=request.user).exclude(peer_reviewer=request.user)
    return render(request, 'challenges/challenges.html', {'challenges': challenges})


@login_required
def new_challenge(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewChallengeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return redirect('challenges')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewChallengeForm()

    return render(request, 'challenges/new_challenge.html', {'form': form})

@login_required
def challenge_detail(request, challenge_id):
    challenge_detail = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'challenges/challenge_detail.html', {'challenge': challenge_detail})

@login_required
def challenge_accepted(request, challenge_id):
    if request.method == 'POST':
        challenge = get_object_or_404(Challenge, pk=challenge_id)
        challenge.peer_reviewer.add(request.user)
        challenge.agreed_number_of_checks = F('agreed_number_of_checks') + 1
        challenge.status = "Started"
        challenge.save()
        return redirect('challenges')


    return render(request, 'challenges/challenges.html')
