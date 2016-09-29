from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'date')
    list_display = ('title', 'date')
    ordering = ['-date', ]

admin.site.register(Post, PostAdmin)
