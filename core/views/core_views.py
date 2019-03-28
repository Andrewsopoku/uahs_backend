

#@login_required(login_url='accounts/signin')
from django.shortcuts import render


def dashboard(request):

    return render(request,'dashboard.html')

