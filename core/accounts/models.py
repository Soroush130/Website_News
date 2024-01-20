from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FavoriteNews(models.Model):
    CATEGORY_NEWS = (
        ("Sports", "Sports"),
        ("Health", "Health"),
        ("Politics", "Politics"),
        ("Economics", "Economics"),
        ("Technology", "Technology"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.CharField(
        max_length=10,
        choices=CATEGORY_NEWS
    )
