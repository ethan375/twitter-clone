from django import forms 
from . models import TwitterUser


class NewTwitterUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = TwitterUser
        fields = [
            'username',
            'password'
        ]