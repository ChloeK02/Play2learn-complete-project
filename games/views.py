from django.shortcuts import render, redirect
from django.http import JsonResponse  # Import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Review



# Existing views rendering templates
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class HomePageView(TemplateView):
    template_name = 'home.html'

class MyAccountView(TemplateView):
    template_name = 'my_account.html'

@login_required
def my_account(request):
    user = request.user
    return render(request, 'my_account.html', {'user': user}) 


def submit_review(request):
    if request.method == 'POST':
        game_name = request.POST.get('game_name')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')


        Review.objects.create(
            user=request.user,
            game_name=game_name,
            review_text=review_text,
            rating=rating
        )

        return redirect('home') 

    return render(request, 'submit_review.html')


