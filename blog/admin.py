from django.contrib import admin
from blog.models import *

admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(BlogTag)