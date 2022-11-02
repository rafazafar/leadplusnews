from django.http import Http404
from django.shortcuts import get_object_or_404, render
from news.serializers import ArticleSerializer
from news.models import Article
from rest_framework import viewsets


def index(request):
    latest_articles_list = Article.objects.order_by('-publishedAt')[:20]
    context = {
        'latest_articles_list': latest_articles_list,
    }
    return render(request, 'index.html', context)


def detail(request, article_id):
    try:
        article = get_object_or_404(Article, pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'article': article})


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.order_by('-publishedAt')[:100]
    serializer_class = ArticleSerializer
