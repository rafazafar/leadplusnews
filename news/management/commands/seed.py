import requests
from django.core.management.base import BaseCommand
from leadplusnews.settings import NEWSAPI_KEY
from news.models import Article


def get_sources():
    url = 'https://newsapi.org/v1/sources'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    sources = r.json()['sources']
    return sources


def get_articles(source):
    url = 'https://newsapi.org/v1/articles'
    params = {
        'source': source,
        'apiKey': NEWSAPI_KEY
    }
    r = requests.get(url, params=params, headers={
        'Content-Type': 'application/json'})
    res = r.json()
    articles = res['articles']
    return articles


def seed_articles():

    for source in get_sources():
        articles = get_articles(source["id"])
        for article in articles:
            if article["description"] is not None:
                try:
                    Article.objects.get(url=article['url'])
                except Article.DoesNotExist:
                    Article.objects.create(
                        author=article['author'],
                        title=article['title'],
                        description=article['description'],
                        url=article['url'],
                        urlToImage=article['urlToImage'],
                        publishedAt=article['publishedAt'],
                    )


def clear_data():
    Article.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_articles()
        print("seeding completed")
