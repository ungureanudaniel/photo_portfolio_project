from django.urls import path
from .views import HomeView, AboutView, ContactView, ServicesView, AddSkillView, CategoryView, EditSpecialtyView, DeleteSpecialtyView

# AddPhotoView, EditPhotoView, DeletePhotoView,
from .forms import AddSpecialtyForm
 # , AddAboutView,

# AllCategoriesView, AddCommentsView, AddCategoryView, ,
urlpatterns = [
    path('', HomeView, name='home'),
    #-----------Photo Category URLs---------------------------------------------
    path('category/<str:slug>', CategoryView, name='category'),
    # path('all_categories/', AllCategoriesView, name='all_categories'),
    path('add_specialty/', AddSpecialtyForm, name='add_specialty'),
    path('edit_category/<str:slug>', EditSpecialtyView, name='edit_category'),
    path('delete_category/<str:slug>', DeleteSpecialtyView, name='delete_category'),
    path('services/', ServicesView, name='services'),
    # path('add_comments/', AddCommentsView, name='add_comments'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
    # -----------Photo URLs------------------------------------------------
    # path('add_photo/', AddPhotoView, name='add_photo'),
    # path('edit_photo/<int:pk>', EditPhotoView, name='edit_photo'),
    # path('delete_photo/<int:pk>', DeletePhotoView, name='delete_photo'),
    # -----------Photo URLs------------------------------------------------

    path('add_skill/', AddSkillView, name='add_skill'),


]
