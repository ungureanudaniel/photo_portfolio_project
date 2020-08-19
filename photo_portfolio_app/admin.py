from django.contrib import admin
from .models import Photo, About, Category, Skills
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_title', 'description', 'date_taken', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')


admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Skills)