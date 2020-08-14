from .models import Category, About, Photo, Tag
from django import forms
import datetime

#-------------GRAB CATEGORIES FROM DATABASE -----------------
choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)
#-------------GRAB CATEGORIES FROM DATABASE -----------------


#-------------ADD CATEGORY FORM -------------------
class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'text', 'thumbnail']

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a name...'}),
            'text': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a description...'}),
        }


#-------------ADD PHOTO FORM --------------------
class AddPhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'image_title', 'category', 'tags']

        widgets = {
            'image_title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a name...'}),
            # 'date_taken': forms.DateTime(),
            'category': forms.Select(choices=choices_list, attrs = {'class': 'form-control'}),

        }
