from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('who_we_are/', views.who_we_are, name='who_we_are'),
    path('what_we_do/', views.what_we_do, name='what_we_do'),
    path('get_in_touch/', views.get_in_touch, name='get_in_touch'),
]
