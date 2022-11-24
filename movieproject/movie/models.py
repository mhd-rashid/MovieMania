from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta():
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def get_url(self):
        return reverse('movie:AllMovieCat',args=[self.slug])

    def __str__(self):
        return self.name



class Movie(models.Model):
    name=models.CharField(max_length=250,unique=True)
    year=models.IntegerField()
    desc=models.TextField()
    image=models.ImageField(upload_to='gallery')
    genres=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name