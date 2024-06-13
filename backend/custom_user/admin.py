from django.contrib import admin

from custom_user import models


class CustomAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CustomUser, CustomAdmin)
