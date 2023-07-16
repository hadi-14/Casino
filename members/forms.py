from django import forms

class User(forms.Form):
    Email = forms.CharField(label="Email", max_length=100)
    Password = forms.CharField(label="Password", max_length=100)
