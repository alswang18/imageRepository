from django.shortcuts import render
from .models import Image


def homepage(request):
    images = Image.objects.order_by('-upload_date')

    context = {'images': images}
    print(context)
    return render(request, "pages/homepage.html", context)
