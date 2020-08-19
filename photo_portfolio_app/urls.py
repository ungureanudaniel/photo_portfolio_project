from django.urls import path
from .views import HomeView, CategoryView, ServicesView, AboutView, ContactView, AddCategoryView, AddPhotoView, AddAboutView, AddSkillsView, SingleView

urlpatterns = [
    path('', HomeView, name='home'),
    path('category/<int:pk>', CategoryView, name='category'),
    path('services/', ServicesView, name='services'),
    path('single/', SingleView, name='single'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('add_category/', AddCategoryView, name='add_category'),
    path('add_photo/', AddPhotoView, name='add_photo'),
    path('add_about/', AddAboutView, name='add_about'),
    path('add_skill/', AddSkillsView, name='add_skill'),


]
