from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import GameHistory, Review
from django.test import TestCase
from django.urls import reverse


# Static templates views
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class LeaderboardTest(TestCase):
    def test_leaderboard_view(self):
        # Create test users and scores
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')

        GameHistory.objects.create(user=user1, score=100)
        GameHistory.objects.create(user=user2, score=150)

        # Get the leaderboard page
        response = self.client.get(reverse('leaderboard'))

        # Check if the leaderboard is rendered and contains the correct scores
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'user2')  # User with the highest score
        self.assertContains(response, '150')   # Score of user2

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
        game_name = request.POST.get('game_name', None)
        game_settings = request.POST.get('game_settings')
        score = int(request.POST.get('score'))
        

        # Save the score to the database
        game_history = GameHistory(
            user=request.user,
            game_name=game_name,
            game_settings=game_settings,
            score=score,
            time_taken=0,
        )
        game_history.save()
        print(f"Score recorded: {game_history.user.username} - {game_history.score}")

        # Fetch the top 10 scores (leaderboard) for the specific game
        leaderboard = GameHistory.objects.filter(game_name=game_name).order_by('-score')[:10]
        leaderboard_data = [
            {
                'username': history.user.username,
                'game_name' : history.game_name,
                'time_taken': history.time_taken,
            }
            for history in leaderboard
        ]

        return JsonResponse({'leaderboard': leaderboard_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def leaderboard(request):
    # Get the top 10 scores (adjust this query as per your model)
    top_scores = GameHistory.objects.order_by('-score')[:10]
    print(top_scores)
    return render(request, 'leaderboard.html', {'leaderboard': top_scores})
