from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    language = models.CharField(default='English', max_length=100)
    rating = models.FloatField(validators=[MaxValueValidator(10), ])
    running_time = models.PositiveIntegerField(help_text="In minutes", default=100)
    owner = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['release_date']

    def __str__(self):
        return self.title
