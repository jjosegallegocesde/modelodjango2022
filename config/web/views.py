import re
from django.shortcuts import render


from web.models import Administradores

# Create your views here.
def Home(request):

    numeroAdmin=Administradores.objects.count()
    administradores=Administradores.objects.all()

    return render(request,'index.html',{'numero':numeroAdmin,'administradores':administradores})
