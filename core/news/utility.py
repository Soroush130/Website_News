from accounts.models import FavoriteNews


def get_favorites_each_user(user):
    favorites_list = [favorite.favorite for favorite in FavoriteNews.objects.filter(user=user)]
    return favorites_list


def normalize_news(news: list):
    News = {
        'Sports': [],
        'Health': [],
        'Politics': [],
        'Economics': [],
        'Technology': [],
    }
    for new in news:
        News[new.category].append(new)

    return remove_key_in_News(News)


def remove_key_in_News(News):
    remove_keys = []
    for key in News.keys():
        if News[key] == []:
            remove_keys.append(key)

    for key in remove_keys:
        News.pop(key)
    return News


def visit_increase_handeler(user, news_single):
    if user not in news_single.view_count_user.all():
        news_single.view_count_user.add(user)
        news_single.view_count += 1
        news_single.save()
    else:
        pass