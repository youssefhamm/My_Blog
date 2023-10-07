from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    nom = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}), 
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email'}),
        required=True
    )
    numero_telephone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'}),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your message'}),
        required=True
    )



    class Meta:
        model = Contact
        fields = ['nom', 'email', 'numero_telephone', 'message']