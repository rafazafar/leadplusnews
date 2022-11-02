from django.core.management.base import BaseCommand
from news.models import Article


def clear_data():
    Article.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        print("All articles deleted")
