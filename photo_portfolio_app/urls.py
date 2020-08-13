from django.urls import path
from .views import HomeView, CategoriesView, ServicesView, AboutView, ContactView

urlpatterns = [
    path('', HomeView, name='home'),
    path('categories/', CategoriesView, name='categories'),
    path('services/', ServicesView, name='services'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),

]
