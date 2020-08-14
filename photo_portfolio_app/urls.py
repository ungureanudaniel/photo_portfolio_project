from django.urls import path
from .views import HomeView, PhotosListView, ServicesView, AboutView, ContactView, AddCategoryView, AddPhotoView

urlpatterns = [
    path('', HomeView, name='home'),
    path('categories/', PhotosListView, name='categories'),
    path('services/', ServicesView, name='services'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    path('add_category/', AddCategoryView, name='add_category'),
    path('add_photo/', AddPhotoView, name='add_photo'),


]
