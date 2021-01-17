from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['upload_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'imageDescription': forms.Textarea(attrs={'class': 'form-control'})
        }
