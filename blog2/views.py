from django.shortcuts import render
from .models import Enspd

# Create your views here.
# pages principales
def home(request):
    return render(request,'index.html')
def epreuve(request):
    return render(request,"epreuves.html")
def correction(request):
    return render(request,"correction.html")

#pages secondaires
def enspd(request):
    list_epreuves=Enspd.objects.all()
    context={'list_epreuves':list_epreuves}
    return render(request,'enspd.html', context)