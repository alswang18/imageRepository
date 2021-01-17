from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['user', 'upload_date']
