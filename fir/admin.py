from django.contrib import admin

from .models import Post
from .models import People


admin.site.register(Post)
admin.site.register(People)

# Register your models here.
