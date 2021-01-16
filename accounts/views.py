from django.shortcuts import render
from django.contrib import messages, auth
from django.conf import settings


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if settings.AUTH_USER_MODEL.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            # if settings.AUTH_USER_MODEL.objects.filter(email=email).exists():
            #     messages.error(request, 'Email is already being used.')
            #     return redirect('register')
            else:
                user = settings.AUTH_USER_MODEL.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'You are registered and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
