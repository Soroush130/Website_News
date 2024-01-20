from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import News
from .utility import get_favorites_each_user, normalize_news, visit_increase_handeler
from .forms import NewsUpdateForm


@login_required(login_url='/accounts/login/')
def home(request):
    user = request.user
    favorites = get_favorites_each_user(user)
    news = News.objects.filter(category__in=favorites).order_by("view_count")
    news = normalize_news(news)
    context = {
        'news': news,
    }
    return render(request, 'news/index.html', context)


@login_required(login_url='/accounts/login/')
def detail_news(request, id):
    user = request.user
    news_single = News.objects.get(id=id)
    visit_increase_handeler(user, news_single)
    context = {
        'news_single': news_single,
    }
    return render(request, 'news/detail_news.html', context)


@login_required(login_url='/accounts/login/')
def news_update(request, id):
    news_single = News.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        category = request.POST.get('category')
        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
        else:
            image = news_single.image

        with transaction.atomic():
            news_single.title = title
            news_single.body = body
            news_single.category = category
            news_single.image = image
            news_single.save()

            return redirect('news:home')
    else:
        news_form = NewsUpdateForm()
    context = {
        'news_form': news_form,
        'news_single': news_single,
    }
    return render(request, "news/news_update.html", context)
