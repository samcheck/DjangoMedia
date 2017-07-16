import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    date_added = models.DateTimeField('Date Added')
    year_released = models.IntegerField(default=0)
    summary = models.CharField(max_length=4096)

    def __str__(self):
        return('{} ({})'.format(self.movie_title, str(self.year_released)))

    def was_added_recently(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=7)
