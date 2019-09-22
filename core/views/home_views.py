from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from core.forms.home_form import LoginForm


def index(request):
    return render(request,'index.html')


def signin(request):

    if request.method == "POST":
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password,)

            if user is not None :

                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('core:dashboard')
            #return redirect('core:dashboard')

            messages.error(request, 'Wrong username or password')




    login_form = LoginForm()
    context = {'login_form':login_form}
    return render(request,'signin.html',context)




def sign_out(request):
    logout(request)
    return redirect('core:signin')


