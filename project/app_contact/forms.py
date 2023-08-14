from django.core.mail import send_mail
from django import forms
from django.template.loader import render_to_string
from core import settings


class ContactForm(forms.Form):
    """Форма на странице контактов"""

    subject = forms.CharField(label="Subject", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
