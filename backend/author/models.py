from django.db import models

from django.db import connection
from django.db import reset_queries

def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func(*args, **kwargs)
        query_info = connection.queries
        print(f'function_name: {func.__name__}')
        print(f'query_count: {len(query_info)}')
        queries = [f'{ query["sql"]}\n' for query in query_info]
        print(f'queries: \n{"".join(queries)}')
        return results
    return inner_func

@database_debug
def regular_query():
    authors = models.Author.objects.all()
    return [author.name for author in authors]

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    # class Meta:
    #     indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return f'{self.name}'

    def get_short_bio(self):
        return f'{self.bio[:100]}...'


class BlogAuthor(Author):
    class Meta:
        proxy = True

    def perform_something(self):
        pass
