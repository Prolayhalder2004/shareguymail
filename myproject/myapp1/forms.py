# file_mailer/forms.py
from django import forms

class FileEmailForm(forms.Form):
    email = forms.EmailField(label='Recipient Email', widget=forms.EmailInput(attrs={'class': 'email-input', 'placeholder': 'Enter your email'}))
    file = forms.FileField(label='File to Send', widget=forms.ClearableFileInput(attrs={'class': 'file-input'}))
