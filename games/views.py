from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Review

# Static templates views
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

# Account view for logged-in users
@login_required
def my_account(request):
    return render(request, 'my_account.html', {'user': request.user}) 

# View to handle review submissions
@login_required
def submit_review(request):
    if request.method == 'POST':
        game_name = request.POST.get('game_name')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')

        # Save the review to the database
        Review.objects.create(
            user=request.user,
            game_name=game_name,
            review_text=review_text,
            rating=rating
        )
        return redirect('thank_you')

    return render(request, 'submit_review.html')

# Thank you page after submitting a review
def thank_you(request):
    return render(request, 'review_thank_you.html')

# Home page displaying reviews
def home(request):
    reviews = Review.objects.all()
    return render(request, 'home.html', {'reviews': reviews})
