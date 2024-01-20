from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    CATEGORY_NEWS = (
        ("Sports", "Sports"),
        ("Health", "Health"),
        ("Politics", "Politics"),
        ("Economics", "Economics"),
        ("Technology", "Technology"),
    )
    title = models.CharField(
        max_length=255
    )
    body = models.TextField()
    view_count_user = models.ManyToManyField(
        User
    )
    view_count = models.PositiveIntegerField(
        default=0
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_NEWS
    )
    image = models.ImageField(
        upload_to="news/",
    )

    class Meta:
        db_table = "News"

    def __str__(self):
        return self.title
