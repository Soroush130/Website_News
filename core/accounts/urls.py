from django.urls import path
from .views import log_in, register, log_out, profile, add_favorite

urlpatterns = [
    path('login/', log_in),
    path('logout/', log_out),
    path('register/', register),
    path('profile/', profile),
    path('add_favorite/', add_favorite),
]
