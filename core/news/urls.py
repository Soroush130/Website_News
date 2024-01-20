from django.urls import path
from .views import home, detail_news, news_update

app_name = 'news'

urlpatterns = [
    # path('', home, name="home"),
    path('detail_news/<int:id>/', detail_news, name="detail"),
    path('news_update/<int:id>/', news_update, name="update"),
]
