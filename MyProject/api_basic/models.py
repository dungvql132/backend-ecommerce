from turtle import title
from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  email = models.CharField(max_length=100)

  def __str__(self):
    return self.email +" "+ self.author
