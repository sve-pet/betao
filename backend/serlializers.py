from rest_framework import serializers

from backend.models import Link


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['link', 'score', 'upvotes', 'downvotes']