from django.urls import path
from . import views
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)