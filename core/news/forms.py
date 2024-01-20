from django.forms import ModelForm
from .models import News


class NewsUpdateForm(ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'body',
            'category',
            'image',
        )