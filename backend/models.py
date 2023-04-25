from django.db import models


class Link(models.Model):
    id = models.IntegerField(primary_key=True)
    link = models.URLField(max_length=250, unique=True)
    score = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField()
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
