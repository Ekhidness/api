# library/models.py
from django.db import models
from django.core.exceptions import ValidationError

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[
        ('fiction', 'Художественная литература'),
        ('textbook', 'Учебник'),
    ])
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    book_file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title

    def clean(self):
        if Book.objects.filter(
            title=self.title,
            author=self.author,
            publication_year=self.publication_year,
            publisher=self.publisher
        ).exclude(pk=self.pk).exists():
            raise ValidationError("Дубликат книги запрещён.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)