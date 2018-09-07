from django import forms

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

    class Meta:
        model = Postulation
        fields = ('name', 'email', 'phone_number', 'motivation','attachments', 'logo',)
