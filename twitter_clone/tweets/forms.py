from django import forms 
from . models import Tweet


class NewTweetForm(forms.ModelForm):

    class Meta:
        model = Tweet 
        fields = [
            'body'
        ]