from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime, date

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = models.FileField(upload_to = "images/", default= "")
    specialties = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to = "images/", default= "")
    image_title = models.CharField(max_length=200)
    date_taken = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100, default=image_title)

    def __str__(self):
        return self.image_title

    class Meta:
        ordering = ["-date_taken"]

    def get_absolute_url(self):
        return reverse('home')

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    # image = models.FileField(upload_to='blog_image', blank=True)
    # text = RichTextField(blank=True, null=True)
    # #text = models.TextField()
    # category = models.CharField(max_length=20, default='recipes')
    # comment_count = models.IntegerField(default=0)
    # views_count = models.IntegerField(default=0)
    # featured = models.BooleanField()
    # #seo_title = models.CharField(max_length=60, blank=True, null=True)
    # #seo_text = models.CharField(max_length=165, blank=True, null=True)
    # #slug = models.SlugField(max_length=255, unique=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # #updated_date = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    # previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    # next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
