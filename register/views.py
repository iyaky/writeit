import os, io
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, CompleteChallenge, FeedbackForm, ChangeChallengeForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.core.files.base import ContentFile
from django.core.files import File
from docx import Document
from django.contrib.auth.models import User
from .models import Profile
from badges.models import Badge
from challenges.models import Challenge
from notification.models import Notification, NotificationType
from django.core.mail import EmailMessage
from django.db.models import F
from challenges.views import new_notification


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
    profile = Profile.objects.get(user = request.user)
    count = 0
    challenges = request.user.completed_peer_reviewer.all()
    for challenge in challenges:
        count += 1
    notifications = request.user.notification_to_user.all()
    unread_count = 0
    for notif in notifications:
        if not notif.read:
            unread_count += 1
    return render(request, 'accounts/profile.html', {'profile': profile, "count": count, "unread": unread_count})

@login_required
def settings(request):
    return render(request, 'settings/profile_settings.html')

@login_required
def my_badges(request):
    my_badges = request.user.badge_users.all()
    not_my_badges = Badge.objects.exclude(badge_users=request.user)
    return render(request, 'my_badges/my_badges.html', {'my_badges': my_badges, 'not_my_badges': not_my_badges})

@login_required
def my_challenges(request):
    challenges = request.user.peer_reviewer.all()
    my_challenges = request.user.challenge_starter.all()
    return render(request, 'my_challenges/my_challenges.html', {'challenges': challenges, 'my_challenges': my_challenges})

@login_required
def my_notifications(request):
    notifications = request.user.notification_to_user.all()
    notifications = notifications.order_by('read')
    unread_count = 0
    for notif in notifications:
        if not notif.read:
            unread_count += 1
    return render(request, 'notifications/my_notifications.html', {'notifications': notifications, 'unread': unread_count})

@login_required
def read_all_notifications(request):
    notifications = request.user.notification_to_user.all()
    for notif in notifications:
        notif.read = True
        notif.save()
    return redirect('my_notifications')

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
            # save reviewed text
            profile = Profile.objects.get(user = request.user)
            if challenge.number_of_checks - challenge.completed_number_of_checks == 1:
                challenge.status = "Completed"
            challenge.completed_number_of_checks = F('completed_number_of_checks') + 1
            challenge.completed_peer_reviewer.add(request.user)

            # manage notifications
            type = NotificationType.objects.get(name= "Complete challenge")
            new_notification(request, request.user.id, type.id)

            form.save()
            #challenge.save()

            # add brownie points to user's profile or post one challenge
            profile = Profile.objects.get(user = request.user)
            profile.peer_review_points = F('peer_review_points') + 1
            profile.save()

            my_challenges = request.user.challenge_starter.all()
            count1 = 0
            count2 = 0
            # count all challenges
            for ch in my_challenges:
                count1 += 1

            # post a challenge if there are pending challenges or count challenges that are not pending
            for my_ch in my_challenges:
                if my_ch.completed_other_challenge == False and my_ch.status == "Pending":
                    my_ch.completed_other_challenge = True
                    print(my_ch.title)
                    my_ch.save()
                    profile.peer_review_points = F('peer_review_points') - 1
                    profile.save()
                    # manage notifications
                    type = NotificationType.objects.get(name= "Create new challenge")
                    new_notification(request, request.user.id, type.id)
                    break
                elif my_ch.completed_other_challenge:
                    count2 += 1

            # notify about new brownie point if no pending challenges were posted instead
            if count1 == count2:
                # manage notifications
                type = NotificationType.objects.get(name= "New brownie point")
                new_notification(request, request.user.id, type.id)

            # create results file and save to model
            if challenge.file_challenge and challenge.status == 'Completed':
                name, extension = os.path.splitext(challenge.uploaded_file.name)
                text = challenge.peer_review_text
                if extension == '.txt':
                    challenge.result_file.save('results.txt', ContentFile(text))
                    challenge.save()
                elif extension == '.docx':
                    result_doc = Document()
                    result_doc.add_paragraph(text)

                    doc_io = io.BytesIO()
                    result_doc.save(doc_io)
                    doc_io.seek(0)

                    # Save the BytesIO to the field here
                    challenge.result_file.save("results.docx", File(doc_io))

                    response = HttpResponse(doc_io.read())
                    response["Content-Disposition"] = "attachment; filename=generated_doc.docx"
                    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    challenge.save()

            # manage badges
            completed_challenges = request.user.completed_peer_reviewer.all()
            count = 0
            for challenge in completed_challenges:
                count += 1

            badges1 = Badge.objects.get(badge_name="Completed 1 challenge")
            badges5 = Badge.objects.get(badge_name="Completed 5 challenges")
            badges20 = Badge.objects.get(badge_name="Completed 20 challenges")
            badges50 = Badge.objects.get(badge_name="Completed 50 challenges")
            badges100 = Badge.objects.get(badge_name="Completed 100 challenges")
            if count == 1 and not request.user in badges1.badge_users.all():
                badges1.badge_users.add(request.user)
                badges1.save()
                # manage notifications
                type = NotificationType.objects.get(name= "New badge")
                new_notification(request, request.user.id, type.id)
            elif count == 5 and not request.user in badges5.badge_users.all():
                badges5.badge_users.add(request.user)
                badges5.save()
                # manage notifications
                type = NotificationType.objects.get(name= "New badge")
                new_notification(request, request.user.id, type.id)
            elif count == 20 and not request.user in badges20.badge_users.all():
                badges20.badge_users.add(request.user)
                badges20.save()
                # manage notifications
                type = NotificationType.objects.get(name= "New badge")
                new_notification(request, request.user.id, type.id)
            elif count == 50 and not request.user in badges50.badge_users.all():
                badges50.badge_users.add(request.user)
                badges50.save()
                # manage notifications
                type = NotificationType.objects.get(name= "New badge")
                new_notification(request, request.user.id, type.id)
            elif count == 100 and not request.user in badges100.badge_users.all():
                badges100.badge_users.add(request.user)
                badges100.save()
                # manage notifications
                type = NotificationType.objects.get(name= "New badge")
                new_notification(request, request.user.id, type.id)

            return redirect('complete_challenge', challenge_id=challenge.id)
    else:
        form = CompleteChallenge(instance=challenge)

    return render(request, 'my_challenges/complete_challenge.html', {'form': form, 'challenge': challenge})

@login_required
def accept_and_close_challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    if request.method == 'POST':

        form = FeedbackForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge.accepted_and_closed = True
            form.save()
            # manage notifications
            type = NotificationType.objects.get(name= "Accept results on challenge")
            new_notification(request, request.user.id, type.id)

            users = challenge.completed_peer_reviewer.all()
            for user in users:
                type = NotificationType.objects.get(name= "Challenge was finished")
                new_notification(request, user.id, type.id)

            return redirect('my_challenges_detail', challenge_id=challenge.id)
    else:
        form = FeedbackForm(instance=challenge)

    return render(request, 'my_challenges/accept_and_close_challenge.html', {'form': form, 'challenge': challenge})

@login_required
def leave_feedback(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    if request.method == 'POST':

        form = FeedbackForm(request.POST, instance=challenge)
        if form.is_valid():
            challenge.accepted_and_closed = True
            form.save()

            return redirect('my_challenges_detail', challenge_id=challenge.id)
    else:
        form = FeedbackForm(instance=challenge)

    return render(request, 'my_challenges/leave_feedback.html', {'form': form, 'challenge': challenge})

@login_required
def dispute_and_reopen(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    #challenge.opened_dispute = True
    #challenge.save()


    return render(request, 'my_challenges/dispute_and_reopen.html', {'challenge': challenge})

@login_required
def manage_dispute(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    challenge.opened_dispute = True
    challenge.status = 'Pending'
    challenge.peer_review_text = challenge.auto_check_text
    challenge.agreed_number_of_checks = 0
    challenge.completed_number_of_checks = 0
    agreed_reviewers = challenge.peer_reviewer.all()
    completed_reviewers = challenge.completed_peer_reviewer.all()
    for reviewer in agreed_reviewers:
        challenge.peer_reviewer.remove(reviewer)
    for reviewer in completed_reviewers:
        challenge.completed_peer_reviewer.remove(reviewer)
    challenge.save()
    # manage notifications
    type = NotificationType.objects.get(name= "Open dispute on challenge")
    new_notification(request, request.user.id, type.id)

    users = challenge.completed_peer_reviewer.all()
    for user in users:
        type = NotificationType.objects.get(name= "Challenge was disputed")
        new_notification(request, user.id, type.id)

    return redirect('my_challenges_detail', challenge_id=challenge.id)

@login_required
def change_challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    if request.method == 'POST':

        form = ChangeChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            form.save()
            # manage notifications
            type = NotificationType.objects.get(name= "Edit challenge")
            new_notification(request, request.user.id, type.id)

            users = challenge.peer_reviewer.all()
            for user in users:
                type = NotificationType.objects.get(name= "Challenge was edited")
                new_notification(request, user.id, type.id)

            return redirect('my_challenges_detail', challenge_id=challenge.id)
    else:
        form = ChangeChallengeForm(instance=challenge)

    return render(request, 'my_challenges/change_challenge.html', {'form': form, 'challenge': challenge})

@login_required
def delete_challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    # manage notifications
    users = challenge.peer_reviewer.all()
    for user in users:
        type = NotificationType.objects.get(name= "Challenge was deleted")
        new_notification(request, user.id, type.id)

    challenge.delete()
    # manage notifications
    type = NotificationType.objects.get(name= "Delete challenge")
    new_notification(request, request.user.id, type.id)

    return redirect('my_challenges')

@login_required
def delete_profile(request):
    user = User.objects.get(pk=request.user.id)
    user.delete()

    return redirect('home')

@login_required
def cant_participate(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    challenge.peer_reviewer.remove(request.user)

    return redirect('my_challenges')
