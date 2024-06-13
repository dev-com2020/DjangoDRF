from django.contrib import admin

from blog import models


class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title']
    show_full_result_count = True
    list_filter = ['title']
    list_display = ['title', 'author', 'word_count']

    def word_count(self, obj):
        return len(obj.content.split())


admin.site.register(models.Blog, BlogAdmin)
