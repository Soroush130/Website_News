from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import LoginUserForm, RegisterUserForm
from .models import FavoriteNews
from .utility import check_favorite

User = get_user_model()


def log_in(request):
    url = request.META.get("HTTP_REFERER")
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect(url)
    else:
        login_form = LoginUserForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            User.objects.create_user(username=username, password=password)
            return redirect('/accounts/login')
    else:
        register_form = RegisterUserForm()

    context = {
        'register_form': register_form,
    }
    return render(request, 'accounts/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get(id=request.user.id)
    favorites = FavoriteNews.objects.filter(user=user)
    context = {
        'user': user,
        'favorites': favorites,
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='/accounts/login/')
def add_favorite(request):
    url = request.META.get("HTTP_REFERER")
    user = request.user
    if request.method == "POST":
        category = request.POST.getlist('category')
        category = check_favorite(category, user)
        objects_to_create = []
        for cate in category:
            objects_to_create.append(
                FavoriteNews(
                    user=user,
                    favorite=cate
                )
            )
        FavoriteNews.objects.bulk_create(objects_to_create)
        return redirect(url)