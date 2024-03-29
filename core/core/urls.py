from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.urls import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),

    path('accounts/', include('accounts.urls')),
    path('news/', include('news.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
