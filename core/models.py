from django.db import models
import datetime

# Create your models here.



class Actor(models.Model):

    name = models.CharField(max_length=100, )
    family_name = models.CharField(max_length=100,)
    birth_date = models.DateField('Birth date', default=None)
    nationality = models.CharField(max_length=100,)
    picture = models.ImageField()
    def __str__(self):
        return f"{self.name} {self.family_name}"  
        
class Film(models.Model):
    title = models.CharField(max_length=100,)
    release_date = models.DateField('release date: ', default=datetime.datetime.now)
    actor = models.ForeignKey(Actor, default=1, verbose_name="Actor", on_delete=models.SET_DEFAULT)
    genre = models.CharField(max_length=100,)

    poster = models.ImageField()
    def __str__(self):
        return self.title  


