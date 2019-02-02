from django import forms
from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Name", required=True,
        help_text="Required."),
    last_name = forms.CharField(label="Last name", required=True,
                     help_text="Required."),
    email = forms.EmailField(label="Email address", required=True,
        help_text="Required.")

    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
