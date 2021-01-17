from django.contrib import admin
from django.urls import path
from .views import homepage, image, upload
from .watermark import addWatermark

urlpatterns = [
    path('', homepage, name='home'),
    path('image/<int:image_id>', image, name='image'),
    path('upload', upload, name='upload')
    # path('search', search, name='search')
]
