from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import GameHistory

# Existing views rendering templates
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class HomePageView(TemplateView):
    template_name = 'home.html'

# View to save game score
@login_required
def save_game_score(request):
    if request.method == 'POST':
        # Get score and game type from the request (sent from Vue)
        score = request.POST.get('score')
        game_type = request.POST.get('game_type')
        
        # Save to GameHistory model
        game_history = GameHistory(user=request.user, score=score, game_type=game_type)
        game_history.save()

        # Return a JSON response indicating success
        return JsonResponse({"status": "success"}, status=200)
    
    # If the method is not POST, return a JSON response indicating failure
    return JsonResponse({"status": "failed"}, status=400)

# View to show leaderboard
def leaderboard(request):
    top_scores = GameHistory.objects.order_by('-score')[:10]  # Get top 10 scores
    return render(request, 'leaderboard.html', {'top_scores': top_scores})
