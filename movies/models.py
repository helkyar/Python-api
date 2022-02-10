from django.db import models

class Genre(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        name = models.CharField(max_length=15)

class Movie(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        model = models.CharField(max_length=25)
        manufacturing_date = models.DateField()
        genre = models.ForeignKey(
            'Genre',
            related_name='movies',
            on_delete=models.CASCADE
        )

        class Meta:
            ordering = ['updated']
            indexes = [models.Index(fields=['genre'])]
