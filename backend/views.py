from django.db.models import F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models import Link
from backend.serlializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Link.objects.all().order_by('link')
    serializer_class = UrlSerializer
    http_method_names = ['get', 'post']

    @action(methods=['post', 'get'], detail=True)
    def upvote(self, request, pk=None):
        Link.objects.filter(pk=pk).update(upvotes=F("upvotes") + 1, score=F("score") + 1)
        serializer = UrlSerializer(Link.objects.get(pk=pk))
        return Response(serializer.data)

    @action(methods=['post', 'get'], detail=True)
    def downvote(self, request, pk=None):
        Link.objects.filter(pk=pk).update(downvotes=F("downvotes") + 1, score=F("score") - 1)
        serializer = UrlSerializer(Link.objects.get(pk=pk))
        return Response(serializer.data)

# Create your views here.
