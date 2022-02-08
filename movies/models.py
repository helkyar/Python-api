from django.db import models

class Genre(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        name = models.CharField(max_length=15)
