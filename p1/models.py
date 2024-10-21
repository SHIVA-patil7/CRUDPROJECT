from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default='untitled')
    author = models.CharField(max_length=100, default='unknown')
    isbn = models.CharField(max_length=13, unique=True, null=True)
    pages = models.IntegerField(default=2)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    language = models.CharField(max_length=20, default='kannada')

    def __str__(self):
        return f"{self.title} by {self.author}"
