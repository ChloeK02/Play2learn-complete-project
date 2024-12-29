from django.urls import path
from .views import save_game_score, leaderboard, MathFactsView, AnagramHuntView
from .views import HomePageView 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('save-score/', save_game_score, name='save_game_score'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('math-facts/', MathFactsView.as_view(), name='math_facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram_hunt'),
]