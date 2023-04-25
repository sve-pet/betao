from django.db.models import F
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models import Link, Comment
from backend.serializer import UrlSerializer, CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UrlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Link.objects.all().order_by('link')
    serializer_class = UrlSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        Link.objects.filter(pk=pk).update(upvotes=F("upvotes") + 1, score=F("score") + 1)
        serializer = UrlSerializer(Link.objects.get(pk=pk))
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        Link.objects.filter(pk=pk).update(downvotes=F("downvotes") + 1, score=F("score") - 1)
        serializer = UrlSerializer(Link.objects.get(pk=pk))
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        link = self.get_object()
        comment = Comment(comment=request.data['comment'], link=link)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

# Create your views here.
