# from django.contrib import admin
# from .models import About, Skill, Comment, Photo, Category
# # Register your models here.
# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('image_title', 'description', 'category', 'date_taken', 'category', 'tags', 'featured')
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'text', 'slug')
#
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'thumbnail', 'headshot')
#
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('skill', 'percentage')
#
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'text', 'date_created', 'approved')
#     list_filter = ('approved', 'date_created')
#     search_fields = ('name', 'email', 'text')
#     actions = ['approve_comments']
#
#
# admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Comment, CommentAdmin)
# # admin.site.register(Tag)
# admin.site.register(About, AboutAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Skill, SkillAdmin)
