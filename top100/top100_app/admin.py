from django.contrib import admin
from .models import Contact, Author, Song, Album, Genre

admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Genre)
