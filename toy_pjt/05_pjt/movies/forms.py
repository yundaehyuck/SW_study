from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:

        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title'
                }
            ),
            'audience': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Audience'
                }
            ),
            'release_date': forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    'class': 'form-control',
                    'placeholder': '연도-월-일',
                    'type': 'date'
                }
            ),
            'genre': forms.Select(
                attrs={
                    'class': 'form-control',
                },
                choices = [(g,g) for g in ['코미디','공포','로맨스']]
            ),
            'score': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Score',
                    'step':0.5,
                    'min':0,
                    'max':5,
                }
            ),
            'poster_url': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Poster url'
                }
            ),
            'description': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Description'
                }
            )
            }
        