from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .models import Category, Photo, Tag, About
from .forms import AddCategoryForm, AddPhotoForm
from django.template.defaultfilters import slugify

#-----------------HOME PAGE--------------------------
def HomeView(request):
    template = 'photo_portfolio_app/home.html'

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, template, context)


#-----------------ADD A NEW PHOTO PAGE--------------------------
def AddPhotoView(request):
    template = 'photo_portfolio_app/add_photo.html'
    common_tags = Photo.tags.most_common()[:4]
    form = AddPhotoForm(request.POST, request.FILES or None)
    if form.is_valid():
        newphoto = form.save(commit=False)
        newphoto.slug = slugify(newphoto.image_title)
        newphoto.save()
        # COMMAND TO SAVE THE FORM USING THE TAGS MANAGER
        form.save_m2m()
        return redirect('/')

    context = {
        'common_tags': common_tags,
        'form': form,
    }
    return render(request, template, context)


#-----------------SERVICES PAGE--------------------------
def ServicesView(request):
    template = 'photo_portfolio_app/services.html'
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, template, context)


#-----------------PHOTOS CATEGORIES PAGE--------------------------
def PhotosListView(request):
    template = 'photo_portfolio_app/categories.html'
    return render(request, template, {})

def AddCategoryView(request):
    template = 'photo_portfolio_app/add_categories.html'
    form = AddCategoryForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, template, context)



#-----------------ABOUT ME PAGE--------------------------
def AboutView(request):
    template = 'photo_portfolio_app/about.html'
    return render(request, template, {})


#-----------------CONTACT ME PAGE--------------------------
def ContactView(request):
    template = 'photo_portfolio_app/contact.html'
    if request.method == "POST":
        message_fname = request.POST['message-fname']
        message_lname = request.POST['message-lname']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        send_mail(
            message_subject,  # subject
            message,  # text
            message_email,  # email
            ['danielungureanu531@gmail.com'], # to email
            fail_silently=False,
        )
        context = {
            'message_fname': message_fname,
            'message_lname': message_lname,
            'message_email': message_email,
            'message_subject': message_subject,
            'message': message,
        }
        return render(request, template, context)


    else:
        #return the page

        return render(request, template, {})
