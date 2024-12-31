from django import forms
from .models import Profile

class ReviewForm(forms.Form):
    GAME_CHOICES = [
        ('math_facts', 'Math Facts'),
        ('anagram_hunt', 'Anagram Hunt'),
    ]
    
    game = forms.ChoiceField(choices=GAME_CHOICES, label='Select Game')
    review = forms.CharField(widget=forms.Textarea, label='Write Your Review')
    rating = forms.IntegerField(min_value=1, max_value=5, label='Rating (1-5)')

class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']