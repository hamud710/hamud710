from django.shortcuts import render
from .models import *
from shop.models import *

def home(request):
    about = AboutUs.objects.order_by("?").first()
    context = {
        'about': about,
        'random': Item.objects.order_by('?').first(),
        'random2': Item.objects.order_by('?').first(),
        'Purchase3': Item.objects.order_by('?')[:3],
        'newProdacts' : Item.objects.all()[:10]
    }
    return render(request, 'index.html',context)

def about(request):
    about = AboutUs.objects.order_by("?").first()
    context = {
        'about': about,
    }
    return render(request,"aboutUs.html",context)
