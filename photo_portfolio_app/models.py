from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# from datetime import datetime, date
# from django.contrib.auth.models import User

# Create your models here.
#
# class Tag(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#----------------------ABOUT MODEL -----------------------------------

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='')
    headshot = models.ImageField(upload_to='')


    def __str__(self):
        return self.title


#----------------------SKILLS MODEL -----------------------------------

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    percentage = models.IntegerField()

    def __str__(self):
        return self.skill

#----------------------PHOTOS CATEGORY MODEL -----------------------------------
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, default="")
    text = models.TextField()
    thumbnail = models.ImageField(upload_to = "static/photo_portfolio_app/categ_images/", default= "")
    specialties = models.BooleanField(blank=True, default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug



    def get_absolute_url(self):
        return reverse('home')

    @property
    def image_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url

#----------------------PHOTOS UPLOAD MODEL -----------------------------------

# class Photo(models.Model):
#     image = models.ImageField(upload_to = "images/", default="")
#     image_title = models.CharField('A short title, max two words', max_length=200)
#     description = models.TextField('A short description...', max_length=500, default="")
# #     # author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#     date_taken = models.DateField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photo', default="")
#     tags = TaggableManager()
#     slug = models.SlugField(unique=True, max_length=100, default="")
#     featured = models.BooleanField('Check this if you want picture to be shown as featured on the home page', default=False)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.image_title)
#         super(Photo, self).save(*args, **kwargs)
#
#
#
#     class Meta:
#         ordering = ["-date_taken"]
#
#     def get_absolute_url(self):
#         return reverse('home')
#
#     def __str__(self):
#         return self.image_title

# --------------------PHOTOS COMMENTS MODEL -----------------------------------
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.text

    def approve(self):
        self.approved = True
        self.save()
