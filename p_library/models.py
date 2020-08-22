from django.db import models

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField(null=True)  
    country = models.CharField(max_length=2, null=True)  
  
    def __str__(self):  
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author'),
    )

# вдохновитель inspirer для автора author при написании книги book
class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
    )