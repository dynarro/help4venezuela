from django import forms
from django.contrib.auth.forms import AuthenticationForm


from .models import Postulation

class PostulationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))

    motivation = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder':"I'm applying this postulation because..."}
    ))
    attachments = forms.FileField(required=False)
    logo = forms.ImageField(required=False)
    class Meta:
        model = Postulation
        fields = ('name', 'email', 'phone_number', 'motivation','attachments', 'logo',)

class LoginForm(AuthenticationForm):
     username = forms.CharField(label="Username", max_length=30,
                                widget=forms.TextInput(attrs={'class':'form-control', 'name': 'username'}))
     password = forms.CharField(label="Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
