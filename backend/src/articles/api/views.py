from rest_framework import viewsets

from articles.models import Article
from .serializers import ArticlesSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticlesSerializer
    queryset = Article.objects.all()


# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView
# )


# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer


# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer


# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer


# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
