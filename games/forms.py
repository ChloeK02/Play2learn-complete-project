from django import forms


class ReviewForm(forms.Form):
    GAME_CHOICES = [
        ('math_facts', 'Math Facts'),
        ('anagram_hunt', 'Anagram Hunt'),
    ]
    
    game = forms.ChoiceField(choices=GAME_CHOICES, label='Select Game')
    review = forms.CharField(widget=forms.Textarea, label='Write Your Review')
    rating = forms.IntegerField(min_value=1, max_value=5, label='Rating (1-5)')

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
