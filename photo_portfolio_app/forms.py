from .models import Category, About, Photo, Skills, Comment
from django import forms
import datetime

#---------------------------------GRAB CATEGORIES FROM DATABASE --------------------------------------------------------
choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)



#--------------------------------------------ADD CATEGORY FORM ---------------------------------------------------------
class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'text', 'thumbnail', 'specialties']

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a name...'}),
            'text': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a description...'}),
        }


#--------------------------------------------ADD PHOTO FORM -----------------------------------------------------------
class AddPhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'image_title', 'description', 'category', 'tags', 'featured']

        widgets = {
            'image_title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a name...'}),
            'description': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a description...'}),
            # 'date_taken': forms.DateTime(),
            'category': forms.Select(choices=choices_list, attrs = {'class': 'form-control'}),
        }

#--------------------------------------------ADD SKILLS FORM -----------------------------------------------------------
class AddSkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ['skill', 'percentage']

        widgets = {
            'skill': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a skill...'}),
            # 'date_taken': forms.DateTime(),
            'percentage': forms.NumberInput(attrs = {'class': 'form-control'}),
        }

#--------------------------------------------ADD ABOUT ME FORM ---------------------------------------------------------
class AddAboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ['title', 'description', 'thumbnail']

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a salute...'}),
            'description': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add a description about yourself...'}),
        }

#--------------------------------------------ADD COMMENT FORM ---------------------------------------------------------
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'text', 'approved']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your bane...'}),
            'email': forms.EmailInput(),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'})
        }
