from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
from django.db.models import Q
from django.contrib.auth.models import User


def homepage(request):
    if request.user.id is None:
        return redirect("login")
    else:
        return redirect("dashboard")


def image(request, image_id):
    image = Image.objects.filter(
        Q(user=request.user.id) | Q(hidden_to_others=False)
    ).filter(pk=image_id)

    if image.exists():
        image = image[0]
    else:
        raise Http404("Image does not exist or is unavailable.")

    context = {
        'image': image
    }

    return render(request, 'images/image.html', context)


def upload(request):
    user = User.objects.filter(pk=request.user.id)
    if user.exists():
        user = user[0]
    else:
        return redirect('login')
    form = ImageForm(initial={'user': user})
    if request.method == 'POST':
        print(request.POST)
        form = ImageForm(request.POST, request.FILES)
        print(form.is_valid())
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
