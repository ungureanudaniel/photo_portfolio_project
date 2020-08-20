from django.contrib import admin
from .models import Photo, About, Category, Skills
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_title', 'description', 'category', 'date_taken', 'category', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'slug')


admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skills)