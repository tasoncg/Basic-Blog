from django.contrib import admin
from .models import Author,Blog,Comment
# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)

