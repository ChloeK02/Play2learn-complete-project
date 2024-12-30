from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import GameHistory, Review


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

def record_score(request):
    if request.method == 'POST':
        game_type = request.POST.get('game_type')
        game_settings = request.POST.get('game_settings')
        score = int(request.POST.get('score'))
        time_taken = int(request.POST.get('time_taken'))

        # Save the score to the database
        game_history = GameHistory(
            user=request.user,
            game_type=game_type,
            game_settings=game_settings,
            score=score,
            time_taken=time_taken,
        )
        game_history.save()

        # Fetch the top 10 scores (leaderboard)
        leaderboard = GameHistory.objects.all().order_by('-score')[:10]  # Get top 10 scores
        leaderboard_data = [
            {
                'username': history.user.username,
                'score': history.score,
                'time_taken': history.time_taken,
            }
            for history in leaderboard
        ]

        return JsonResponse({'leaderboard': leaderboard_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def leaderboard(request):
    # Fetch the top 10 scores
    leaderboard = GameHistory.objects.all().order_by('-score')[:10]
    leaderboard_data = [
        {
            'username': history.user.username,
            'score': history.score,
            'time_taken': history.time_taken,
        }
        for history in leaderboard
    ]
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard_data})