from rest_framework import serializers

from backend.models import Link, Comment


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['link', 'score', 'upvotes', 'downvotes']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']