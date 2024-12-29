from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_type = models.CharField(max_length=100)
    score = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game_type} - {self.score}"