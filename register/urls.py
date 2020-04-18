from django.conf.urls import url
from . import views

urlpatterns = [
    #url('', views.usersignup, name='register_user'),
    url('profile/',views.profile, name='profile'),
    url('settings/', views.settings, name='profile_settings'),
    url('my_badges', views.my_badges, name='my_badges'),
    url('my_challenges', views.my_challenges, name='my_challenges'),
]
