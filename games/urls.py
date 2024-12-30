from django.urls import path
from .views import MathFactsView, AnagramHuntView
from . import views 

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('', views.home, name='home'),
    path('math-facts/', MathFactsView.as_view(), name='math_facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram_hunt'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]