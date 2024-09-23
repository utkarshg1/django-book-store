from django.db import models


class book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
