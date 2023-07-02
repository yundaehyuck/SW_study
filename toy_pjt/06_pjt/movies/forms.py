from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title', 'description',)
        widgets = {

            'description': forms.Textarea(attrs={'cols':40, 'rows':5}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie', 'user',)