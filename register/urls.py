from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url('', views.usersignup, name='register_user'),
    url('profile/',views.profile, name='profile'),
    url('settings/', views.settings, name='profile_settings'),
    url('change_settings', views.change_settings, name='change_settings'),
    url('my_badges', views.my_badges, name='my_badges'),
    url('my_challenges', views.my_challenges, name='my_challenges'),
    path('<int:challenge_id>/', views.my_challenges_detail, name='my_challenges_detail'),
    path('<int:challenge_id>/complete_challenge/', views.complete_challenge, name='complete_challenge'),
    path('<int:challenge_id>/leave_feedback/', views.leave_feedback, name='leave_feedback'),
]
