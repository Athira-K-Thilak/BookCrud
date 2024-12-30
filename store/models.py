from django.db import models

# Create your models here.

#Book[id,title,author,price,language,genre,year]

class Book(models.Model):

    title=models.CharField(max_length=200)

    author=models.CharField(max_length=250)

    price=models.PositiveIntegerField()

    language=models.CharField(max_length=200)

    genre=models.CharField(max_length=100)

    year=models.CharField(max_length=10)

    def __str__(self):
        
        return self.title