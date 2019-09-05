from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import AlbumForm, ContactForm
from .models import Album, Contact
from django.contrib.auth import update_session_auth_hash


def index(request):
    album = Album.objects.all()
    return render(request, 'website/index.html', {'album': album})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email, username=username) is not True:
                user = User.objects.create_user(email=email, username=username, password=password1)
                user.save()
                messages.info(request, 'USER CREATED')
                return render(request, 'website/register.html')
            else:
                messages.info(request, 'USER ALREADY EXIST')
                return render(request, 'website/register.html')
        else:
            messages.info(request, 'PASSWORD IS NOT MATCHING')
            return render(request, 'website/register.html')
    else:
        return render(request, 'website/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'website/index.html')
        else:
            messages.info(request, 'USERNAME OR PASSWORD IS INCORRECT')
            return render(request, 'website/login.html')
    else:
        return render(request, 'website/login.html')


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AlbumForm()
            messages.info(request, 'THANK YOU !!!')
            return render(request, 'website/add_album.html', {'form': form})
        else:
            return render(request, 'website/add_album.html')
    else:
        return render(request, 'website/add_album.html')


def album_store(request):
    if request.user.is_authenticated:
        album = Album.objects.all()
        return render(request, 'website/albums-store.html', {'album': album})
    else:
        messages.info(request, 'PLEASE LOGIN FIRST')
        return render(request, 'website/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'website/index.html')


def change_password(request):
    if request.method == 'POST':
        user = request.user
        new_password = request.POST.get('new_password')
        con_password = request.POST.get('con_password')
        if new_password == con_password:
            user = User.objects.get(username=user.username)
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.info(request, 'PASSWORD CHANGED')
            return render(request, 'website/change_password.html')
        else:
            messages.info(request, 'PASSWORD IS NOT MATCHING')
            return render(request, 'website/change_password.html')
    else:
        return render(request, 'website/change_password.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'THANK YOU !!!')
            return render(request, 'website/contact.html')
        else:
            messages.info(request, 'INFORMATION IS INCORRECT')
            return render(request, 'website/contact.html')
    else:
        return render(request, 'website/contact.html')








