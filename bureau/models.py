from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()


class NewsPaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_year = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor)

    def __str__(self):
        return self.title
