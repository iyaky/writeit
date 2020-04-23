from django.urls import path
from . import views

urlpatterns = [
    path('',views.challenges, name='challenges'),
    path('<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('new_challenge/', views.new_challenge, name='new_challenge'),
    path('challenge_accepted/', views.challenge_accepted, name='challenge_accepted'),
]
