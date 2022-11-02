import datetime
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, default='title')
    description = models.TextField(default='description')
    url = models.CharField(max_length=200, blank=True, null=True)
    urlToImage = models.CharField(max_length=200, blank=True, null=True)
    publishedAt = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.publishedAt >= timezone.now() - datetime.timedelta(days=1)
