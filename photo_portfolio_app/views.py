
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import About, Skill, Category
# Photo, Comment, Category,
from .forms import AddSpecialtyForm, CommentForm
# AddPhotoForm
# AddAboutForm, , AddCategoryForm, ,
from django.template.defaultfilters import slugify
from django.db.models import Count


#-----------------CATEGORY COUNT--------------------------
# def get_category_count():
#     queryset = Photo.objects.values_list('category').annotate(Count('category'))
#     count = queryset.values('category', 'category__count')
#     return count

#-----------------HOME PAGE-----------------------------
def HomeView(request):
    template = 'photo_portfolio_app/home.html'
    # category_count = get_category_count()
    # print(category_count)
    about = About.objects.all()[:1]
    # other_specialty = Category.objects.filter(specialties=False)
    # specialty = Skills.objects.filter(specialties=True)
    # first_three_photos = Photo.objects.filter(featured=True)[:3]
    # next_three_photos = Photo.objects.filter(featured=True)[3:6]
    # last_three_photos = Photo.objects.filter(featured=True)[6:9]
    # featured_pics = Photo.objects.filter(featured=True)
    # firsttwo_specialties = Category.objects.filter(specialties=True)[:2]
    categories_specialty = Category.objects.filter(specialties=True)
    # lasttwo_specialties = Category.objects.filter(specialties=True)[2:4]

    cat_menu = Category.objects.all()
    # print(cat_menu)

    if request.method == "POST":
        try:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # Save the comment to the database
                comment_form.save()
        except Error as e:
            print(e)
    else:
        comment_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'about': about,
        "categories_specialty": categories_specialty,
        'cat_menu': cat_menu,
        # "featured_pics": featured_pics,
        # 'firsttwo_specialties': firsttwo_specialty,
        # 'lasttwo_specialties': lasttwo_specialty,
        # 'first_three_photos': first_three_photos,
        # 'next_three_photos': next_three_photos,
        # 'last_three_photos': last_three_photos,
        # 'category_count': category_count,
        # 'other_specialty': other_specialty,
        # 'specialty': specialty,
    }
    return render(request, template, context)


#----------------------ADD A NEW PHOTO PAGE------------------------------------
def AddPhotoView(request):
    template = 'photo_portfolio_app/add_photo.html'
    about = About.objects.all()[:1]
    # common_tags = Photo.tags.most_common()[:4]
    # cat_menu = Category.objects.all()

    form = AddPhotoForm(request.POST or None)
    if form.is_valid():
    # COMMAND TO SAVE THE FORM USING THE TAGS MANAGER
        form.save()
        return redirect('/')

    context = {
        'about': about,
        # 'cat_menu': cat_menu,
        # 'common_tags': common_tags,
        'form': form,
    }
    return render(request, template, context)


#-----------------------------EDIT PHOTO --------------------------------------
def EditPhotoView(request, pk):
    template = 'photo_portfolio_app/edit_photo.html'
    # specific_photo_grab = Photo.objects.get(id=pk)
    form = AddPhotoForm(instance=specific_photo_grab)
    if request.method == "POST":
        form = AddCategoryForm(request.POST or None, request.FILES or None, instance=specific_photo_grab)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'about': about,
        'form': form,
        # 'specific_photo_grab': specific_photo_grab,
    }
    return render(request, template, context)


#-----------------------------DELETE PHOTO -------------------------------------
def DeletePhotoView(request, slug):
    template = 'photo_portfolio_app/delete_photo.html'
    # fetch the object related to passed slug
    category = Category.objects.get(slug=slug)

    if request.method == "POST":
        category.delete()
        # messages.success(request, 'Category has been deleted!')
        return redirect("/")

    context = {
        'about': about,
        'category': category,
    }
    return render(request, template, context)

#-----------------SERVICES PAGE--------------------------
def ServicesView(request):
    template = 'photo_portfolio_app/services.html'
    other_specialty = Category.objects.filter(specialties=False)
    specialty = Category.objects.filter(specialties=True)
    about = About.objects.all()[:1]
    # cat_menu = Category.objects.all()
    context = {
        'about': about,
        # 'cat_menu': cat_menu,
        'specialty': specialty,
        'other_specialty': other_specialty,
    }
    return render(request, template, context)


#-----------------PHOTOS SINGLE CATEGORY PAGE--------------------------
def CategoryView(request, slug):
    template = 'photo_portfolio_app/category.html'
    specialties = Category.objects.filter(specialties=True)
    category = get_object_or_404(Category, slug=slug)
    # photos_by_category = Photo.objects.filter(category=category)
    # category_count = get_category_count()
    # print(category_count)
    # print(category)
    about = About.objects.all()[:1]
    cat_menu = Category.objects.all()
    context = {
        'about': about,
        'slug': slug,
        'category': category,
        'cat_menu': cat_menu,
        'specialties': specialties,
        # 'photos_by_category': photos_by_category,
    }
    return render(request, template, context)

#-----------------PHOTOS ALL CATEGORIES PAGE--------------------------
# def AllCategoriesView(request):
#     template = 'photo_portfolio_app/all_categories.html'
#     specialty = Category.objects.filter(specialties=True)
#     all_photos = Photo.objects.all()
#     category_count = get_category_count()
#     # print(category_count)
#     print(category_count)
#     about = About.objects.all()[:1]
#     cat_menu = Category.objects.all()
#     context = {
#         'about': about,
#         'all_photos': all_photos,
#         'cat_menu': cat_menu,
#         'specialty': specialty,
#     }
#     return render(request, template, context)

def AddSpecialtyForm(request):
    template = 'photo_portfolio_app/add_specialty.html'
    about = About.objects.all()[:1]
    form = AddSpecialtyForm(request.POST)
    # cat_menu = Category.objects.all()

        # specialty_name = request.POST.get('specialty_name')
        # specialty_descr = request.POST.get('specialty_descr')
        # specialty_thumbnail = request.POST.get('specialty_thumbnail')
        # specialty_show = request.POST.get('specialty_show')
        # newspecialty.slug = slugify(newspecialty.specialty_name)
        # messages.success(request, specialty_name)
        # newspecialty = Category(name=specialty_name, slug=slugify(specialty_name), text=specialty_descr, thumbnail=specialty_thumbnail, specialties=specialty_show)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'about': about,
        "form": form,
        # 'cat_menu': cat_menu,
    }
    return render(request, template, context)

#-----------------------------EDIT CATEGORIES ----------------------------------
def EditSpecialtyView(request, slug):
    template = 'photo_portfolio_app/edit_category.html'
    about = About.objects.all()[:1]
    category = Category.objects.get(slug=slug)
    form = AddCategoryForm(instance=category)
    if request.method == "POST":
        form = AddCategoryForm(request.POST or None, request.FILES or None, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'about': about,
        'form': form,
        'category': category,
    }
    return render(request, template, context)


#-----------------------------DELETE CATEGORIES --------------------------------
def DeleteSpecialtyView(request, slug):
    template = 'photo_portfolio_app/delete_category.html'
    about = About.objects.all()[:1]
    # fetch the object related to passed slug
    category = Category.objects.get(slug=slug)

    if request.method == "POST":
        category.delete()
        # messages.success(request, 'Category has been deleted!')
        return redirect("/")

    context = {
        'about': about,
        'category': category,
    }
    return render(request, template, context)

#-----------------ABOUT ME PAGE--------------------------
def AboutView(request):
    template = 'photo_portfolio_app/about.html'
    about = About.objects.all().order_by('-id')
    skills = Skill.objects.all().order_by('-percentage')
    # cat_menu = Category.objects.all()
    context = {
        # 'cat_menu': cat_menu,
        'skills': skills,
        'about': about,
    }
    return render(request, template, context)
#-----------------ADD ABOUT ME PAGE--------------------------
def AddAboutView(request):
    template = 'photo_portfolio_app/add_about.html'
    about = About.objects.all()[:1]
    form = AddAboutForm(request.POST, request.FILES or None)
    # cat_menu = Category.objects.all()
    if form.is_valid():
        about = form.save(commit=False)
        about.slug = slugify(about.title)
        about.save()
        # COMMAND TO SAVE THE FORM USING THE TAGS MANAGER
        form.save()
        return redirect('/')

    context = {
        'about': about,
        # 'cat_menu': cat_menu,
        'form': form,
    }
    return render(request, template, context)


def AddSkillView(request):
    template = 'photo_portfolio_app/add_skills.html'
    about = About.objects.all()[:1]
    # form = AddSkillForm(request.POST, request.FILES or None)
    # cat_menu = Category.objects.all()
    if request.method == 'POST':
        skill_name = request.POST.get('skill')
        perc_value = request.POST.get('perc')
        messages.success(request, skill_name)
        newskill = Skill(skill=skill_name, percentage=perc_value)
        # newskill.slug = slugify(newskill.skill)
        newskill.save()

        return redirect('/')
        # except Exception as e:
        #     messages.warning(request, e)

        context = {
            'about': about,
            # 'cat_menu': cat_menu,
            'form': form,
        }
    else:
        context = {
            'about': about,
            # 'cat_menu': cat_menu,
        }
    return render(request, template, context)




# def AddCommentsView(request):
#     template = 'photo_portfolio_app/add_comment.html'
#     about = About.objects.all()[:1]
#     comment_form = CommentForm(request.POST or None)
#     # if comment_form.is_valid():
#     #     comment_form.save()
#     #     return redirect('home')
#     # else:
#     #     comment_form = CommentForm()
#
#     context = {
#         'comment_form': comment_form,
#         'about': about,
#     }
#     return render(request, template, context)


#-----------------CONTACT ME PAGE--------------------------
def ContactView(request):
    template = 'photo_portfolio_app/contact.html'
    about = About.objects.all()[:1]
    # cat_menu = Category.objects.all()
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
            'about': about,
            # 'cat_menu': cat_menu,
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
