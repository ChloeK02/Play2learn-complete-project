from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

   
    game_name = models.CharField(max_length=100)

    review_text = models.TextField()

   
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 

    def __str__(self):
        return f"Review by {self.user.username} for {self.game_name}"   

    
