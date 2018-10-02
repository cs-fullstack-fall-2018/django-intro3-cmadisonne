from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=200)
    stars = models.CharField(max_length=200)
    releaseDate = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return ('Name: %s, Stars: %s , Published: %s' %(self.name, self.stars, self.releaseDate))


# Create your models here.
