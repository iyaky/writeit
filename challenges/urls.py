from django.urls import path
from . import views

urlpatterns = [
    path('',views.challenges, name='challenges'),
    path('<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('choose_challenge_type/', views.choose_challenge_type, name='choose_challenge_type'),
    path('plain_text_challenge/', views.plain_text_challenge, name='plain_text_challenge'),
    path('file_challenge/', views.file_challenge, name='file_challenge'),
    path('<int:challenge_id>/peer_review_others/', views.peer_review_others, name='peer_review_others'),
    path('challenge_accepted/<int:challenge_id>/', views.challenge_accepted, name='challenge_accepted'),
]
