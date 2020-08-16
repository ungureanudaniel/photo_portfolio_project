from django.urls import path
from .views import HomeView, PhotosListView, ServicesView, AboutView, ContactView, AddCategoryView, AddPhotoView, AddAboutView, AddSkillsView

urlpatterns = [
    path('', HomeView, name='home'),
    path('categories/', PhotosListView, name='categories'),
    path('services/', ServicesView, name='services'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('add_category/', AddCategoryView, name='add_category'),
    path('add_photo/', AddPhotoView, name='add_photo'),
    path('add_about/', AddAboutView, name='add_about'),
    path('add_skill/', AddSkillsView, name='add_skill'),


]
