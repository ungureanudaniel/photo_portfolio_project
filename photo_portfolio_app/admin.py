from django.contrib import admin
from .models import Photo, About, Category, Skills
# Register your models here.

admin.site.register(Photo)
# admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Skills)