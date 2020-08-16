from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .models import Category, Photo, About, Skills
from .forms import AddCategoryForm, AddPhotoForm, AddAboutForm, AddSkillsForm
from django.template.defaultfilters import slugify
from django.db.models import Count


#-----------------CATEGORY COUNT--------------------------
def get_category_count():
    queryset = Photo.objects.values_list('category').annotate(Count('category'))
    count = queryset.values('category', 'category__count')
    return count

#-----------------HOME PAGE-----------------------------
def HomeView(request):
    template = 'photo_portfolio_app/home.html'
    category_count = get_category_count()

    other_specialty = Category.objects.filter(specialties=False)
    specialty = Category.objects.filter(specialties=True)
    first_three_photos = Photo.objects.filter(featured=True)[:3]
    next_three_photos = Photo.objects.filter(featured=True)[3:6]
    last_three_photos = Photo.objects.filter(featured=True)[6:9]

    firsttwo_specialty = Category.objects.filter(specialties=True)[:2]
    lasttwo_specialty = Category.objects.filter(specialties=True)[2:4]

    context = {
        'firsttwo_specialty': firsttwo_specialty,
        'lasttwo_specialty': lasttwo_specialty,
        'first_three_photos': first_three_photos,
        'next_three_photos': next_three_photos,
        'last_three_photos': last_three_photos,
        'category_count': category_count,
        'other_specialty': other_specialty,
        'specialty': specialty,
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
    other_specialty = Category.objects.filter(specialties=False)
    specialty = Category.objects.filter(specialties=True)
    context = {
        'specialty': specialty,
        'other_specialty': other_specialty,
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



#-----------------ADD ABOUT ME PAGE--------------------------
def AddAboutView(request):
    template = 'photo_portfolio_app/add_about.html'
    form = AddAboutForm(request.POST, request.FILES or None)
    if form.is_valid():
        about = form.save(commit=False)
        about.slug = slugify(about.title)
        about.save()
        # COMMAND TO SAVE THE FORM USING THE TAGS MANAGER
        form.save()
        return redirect('about')

    context = {
        'form': form,
    }
    return render(request, template, context)


def AddSkillsView(request):
    template = 'photo_portfolio_app/add_skills.html'
    form = AddSkillsForm(request.POST, request.FILES or None)
    if form.is_valid():
        newskill = form.save(commit=False)
        newskill.slug = slugify(newskill.skill)
        newskill.save()
        # COMMAND TO SAVE THE FORM USING THE TAGS MANAGER
        form.save()
        return redirect('add_skill')

    context = {
        'form': form,
    }
    return render(request, template, context)


#-----------------ABOUT ME PAGE--------------------------
def AboutView(request):
    template = 'photo_portfolio_app/about.html'
    about_me = About.objects.all().order_by('-id')
    skills = Skills.objects.all().order_by('-percentage')

    context = {
        'skills': skills,
        'about_me': about_me,
    }
    return render(request, template, context)


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
