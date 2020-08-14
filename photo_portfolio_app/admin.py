from django.contrib import admin
from .models import Photo, Tag, About, Category
# Register your models here.

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Category)