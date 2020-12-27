from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length = 100, default='Name')
    phone = models.CharField(max_length = 13, default='Name')
    mail = models.CharField(max_length = 100)
    message = models.CharField(max_length = 2000)

    def __str__(self):
        return self.mail

class Genre(models.Model):
    name = models.CharField(max_length = 30, default='Name')
    description = models.CharField(max_length = 300, default='Description')
    image = models.ImageField(upload_to='top100_app/static/images/genres', blank=True, null=False, verbose_name='Image')
    

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 30, default='Name')
    info = models.CharField(max_length = 200, default='Information')
    image = models.ImageField(upload_to='top100_app/static/images/authors', blank=True, null=True, verbose_name='Image')

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length = 20)
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null = True)
    repros = models.IntegerField()
    image = models.ImageField(upload_to='top100_app/static/images/albums', verbose_name='Image', null = True, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=20)
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null = True)
    repros = models.IntegerField()
    date = models.DateTimeField(default = datetime.now)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name