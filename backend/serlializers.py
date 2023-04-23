from rest_framework import serializers

from backend.models import Url


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ['url', 'score', 'upvotes','downvotes']

