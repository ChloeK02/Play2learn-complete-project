from django.urls import path
from .views import MathFactsView, AnagramHuntView
from .views import HomePageView 
from . import views 

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('', HomePageView.as_view(), name='home'),
    path('math-facts/', MathFactsView.as_view(), name='math_facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram_hunt'),
    path('submit-review/', views.submit_review, name='submit_review'),
]