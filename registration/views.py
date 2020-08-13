from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    template = 'registration/login.html'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("login")
            print()
        else:
            return redirect("login")
    else:
        return render(request, template, {})

def logout_view(request):
    logout(request)
    return redirect('/')