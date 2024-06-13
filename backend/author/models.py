from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BlogAuthor(Author):
    class Meta:
        proxy = True

    def perform_something(self):
        pass
