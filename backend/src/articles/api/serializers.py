from rest_framework import serializers

from articles.models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')
