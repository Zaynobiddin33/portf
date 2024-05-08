from django.db import models

# Create your models here.

class Techs(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Image(models.Model):
    image = models.ImageField()

class Media(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    image = models.ImageField()

class AboutMe(models.Model):
    text = models.TextField()

class Messages(models.Model):
    email = models.EmailField()
    text = models.TextField()

class Project(models.Model):
    domain = models.CharField(max_length=200)
    link = models.URLField()
    techs = models.TextField()
