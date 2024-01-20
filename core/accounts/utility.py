from .models import FavoriteNews


def check_favorite(favorites_list: list, user) -> list:
    exists_favorite = [favorite.favorite for favorite in FavoriteNews.objects.filter(user=user)]

    category = []
    for favorite in favorites_list:
        if favorite not in exists_favorite:
            category.append(favorite)
        else:
            pass

    return category
