
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, CompleteChallenge, FeedbackForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from .models import Profile
from badges.models import Badge
from challenges.models import Challenge
from django.core.mail import EmailMessage
from django.db.models import F

def usersignup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('accounts/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activated successfully!')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def change_settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_settings')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'settings/change_settings.html', context)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def settings(request):
    return render(request, 'settings/profile_settings.html')

@login_required
def my_badges(request):
    badges = Badge.objects
    return render(request, 'my_badges/my_badges.html', {'badges': badges})


@login_required
def my_challenges(request):
    challenges = request.user.peer_reviewer.all()
    my_challenges = request.user.challenge_starter.all()
    return render(request, 'my_challenges/my_challenges.html', {'challenges': challenges, 'my_challenges': my_challenges})

@login_required
def my_challenges_detail(request, challenge_id):
    my_challenges_detail = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'my_challenges/my_challenges_detail.html', {'challenge': my_challenges_detail})


@login_required
def complete_challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    if request.method == 'POST':

        form = CompleteChallenge(request.POST, instance=challenge)
        if form.is_valid():
            challenge.completed_number_of_checks = F('completed_number_of_checks') + 1
            challenge.completed_peer_reviewer.add(request.user)
            form.save()

            return redirect('complete_challenge', challenge_id=challenge.id)
    else:
        form = CompleteChallenge(instance=challenge)

    return render(request, 'my_challenges/complete_challenge.html', {'form': form, 'challenge': challenge})

@login_required
def leave_feedback(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    if request.method == 'POST':

        form = FeedbackForm(request.POST, instance=challenge)
        if form.is_valid():
            form.save()

            return redirect('my_challenges_detail', challenge_id=challenge.id)
    else:
        form = FeedbackForm(instance=challenge)

    return render(request, 'my_challenges/leave_feedback.html', {'form': form, 'challenge': challenge})
