from django.db import models
from django.db.models.base import Model

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class About(models.Model):
    para =  models.TextField(null=True)
    p1n = models.CharField(max_length=50) 
    p1i = models.CharField(max_length=100)
    p2n = models.CharField(max_length=50) 
    p2i = models.CharField(max_length=100)

    def __str__(self):
        return self.para

class Members(models.Model):
    name = models.CharField( max_length=50 , null=True)
    email = models.EmailField( max_length=254,null=True)
    num = models.IntegerField(max_length=10,null=True)
    msg = models.TextField(null=True)

    def __str__(self):
        return self.name



class Home(models.Model):
    fb = models.URLField(max_length=200)
    twit = models.URLField(max_length=200)
    insta = models.URLField(max_length=200)

    def __str__(self):
        return self.fb


