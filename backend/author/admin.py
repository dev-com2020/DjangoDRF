from django.contrib import admin

from author import models


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Author, AuthorAdmin)
