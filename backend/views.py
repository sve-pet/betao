from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from backend.models import Url
from backend.serlializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Url.objects.all().order_by('url')
    serializer_class = UrlSerializer
    http_method_names = ['get', 'post']

    @action(methods=['post'], detail=True)
    def upvote(self, request, pk=None):
        Url.objects.filter(pk=pk).update(upvotes=F("upvotes") + 1, score=F("score")+1)
        serializer = UrlSerializer(Url.objects.get(pk=pk))
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def downvote(self, request, pk=None):
        Url.objects.filter(pk=pk).update(downvotes=F("downvotes") + 1, score=F("score") - 1)
        serializer = UrlSerializer(Url.objects.get(pk=pk))
        return Response(serializer.data)





from django.shortcuts import render

# Create your views here.
