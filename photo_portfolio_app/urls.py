from django.urls import path
from .views import HomeView, CategoryView, ServicesView, AboutView, ContactView, \
    AddCategoryView, AddPhotoView, AddAboutView, AddSkillsView, SingleView, EditCategoryView, \
    DeleteCategoryView, EditPhotoView, DeletePhotoView, AllCategoriesView

urlpatterns = [
    path('', HomeView, name='home'),
    #-----------Photo Category URLs------------------------------------------------
    path('category/<str:slug>', CategoryView, name='category'),
    path('all_categories/', AllCategoriesView, name='all_categories'),
    path('add_category/', AddCategoryView, name='add_category'),
    path('edit_category/<str:slug>', EditCategoryView, name='edit_category'),
    path('delete_category/<str:slug>', DeleteCategoryView, name='delete_category'),
    path('services/', ServicesView, name='services'),
    path('single/', SingleView, name='single'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    # -----------Photo URLs------------------------------------------------
    path('add_photo/', AddPhotoView, name='add_photo'),
    path('edit_photo/<int:pk>', EditPhotoView, name='edit_photo'),
    path('delete_photo/<int:pk>', DeletePhotoView, name='delete_photo'),
    # -----------Photo URLs------------------------------------------------

    path('add_about/', AddAboutView, name='add_about'),
    path('add_skill/', AddSkillsView, name='add_skill'),


]
