from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError

#-----------------HOME PAGE--------------------------
def HomeView(request):
    template = 'photo_portfolio_app/home.html'
    return render(request, template, {})


#-----------------ADD A NEW PHOTO PAGE--------------------------
def AddPhotoView(request):
    template = 'photo_portfolio_app/home.html'
    return render(request, template, {})


#-----------------SERVICES PAGE--------------------------
def ServicesView(request):
    template = 'photo_portfolio_app/services.html'
    return render(request, template, {})


#-----------------PHOTOS CATEGORIES PAGE--------------------------
def CategoriesView(request):
    template = 'photo_portfolio_app/categories.html'
    return render(request, template, {})


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
