from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image


def homepage(request):
    if request.user.id is None:
        return redirect("login")
    else:
        return redirect("dashboard")


def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id, user=request.user.id)

    context = {
        'image': image
    }

    return render(request, 'images/image.html', context)


def upload(request):
    form = ImageForm()
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form Saved")
            return redirect('dashboard')
    count = Image.objects.filter(user=request.user.id).count()
    context = {'count': count, 'form': form}
    return render(request, 'images/upload.html', context)

# def search(request):
#     queryset_list = Image.objects.order_by('-upload_date')

#     if 'keywords' in r
