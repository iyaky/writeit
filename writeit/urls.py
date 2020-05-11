"""writeit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
import home.views
import register.views
import challenges.views
import badges.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', home.views.home, name='home'),
    path('about/', include('home.urls')),
    path("register/", register.views.usersignup, name="register"),
    path("register/sent_link/", register.views.sent_link, name="sent_link"),
    path("login/", register.views.login, name="login"),
    #url('accounts/', include('social_django.urls', namespace='social')),
    path('accounts/', include('register.urls')),
    path('challenges/', include('challenges.urls')),
    #path('challenges/', challenges.views.challenges, name="challenges"),
    path('plain_text_challenge/', challenges.views.plain_text_challenge, name="plain_text_challenge"),
    path('file_challenge/', challenges.views.file_challenge, name='file_challenge'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        register.views.activate_account, name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/successful_registration/$', register.views.successful_registration, name="successful_registration"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/invalid_link/$', register.views.invalid_link, name="invalid_link"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
