from django import forms

from .models import Postulation

class PostulationForm(forms.ModelForm):

    class Meta:
        model = Postulation
        fields = ('name', 'email', 'phone_number', 'motivation','attachments', 'logo',)
