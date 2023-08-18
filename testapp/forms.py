from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1' ,'password2', 'first_name', 'last_name')

def save(self, commit=True):
    user = super(UserForm, self).save(commit=False)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    if commit:
            user.save()
    return user