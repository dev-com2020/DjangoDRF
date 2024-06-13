from django.contrib import admin

from blog import models


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Blog, BlogAdmin)
