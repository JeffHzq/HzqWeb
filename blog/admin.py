from django.contrib import admin
from blog.models import *
from blog.form import BlogForm

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'create_time', 'tags')
    form = BlogForm

admin.site.register(BlogType)
admin.site.register(Blog, BlogAdmin)
