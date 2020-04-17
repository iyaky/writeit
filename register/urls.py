from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.usersignup, name='register_user'),
]
