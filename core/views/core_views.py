

#@login_required(login_url='accounts/signin')
from django.shortcuts import render

from core.models.ambulance_service import AmbulanceService


def dashboard(request):


    return render(request,'dashboard.html')

def ambulance_service_detail(request,pk):
    ambulance_service = AmbulanceService.objects.get(id=pk)

    context = {"abulance_service":ambulance_service}
    return render(request, 'ambulance_service_detail.html',context)

