from django.db import models


class Url(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=250, unique=True)
    score = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
