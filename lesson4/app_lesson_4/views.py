from django.shortcuts import render
from .models import Adverisement

def index(request):
    advertisements = Adverisement.objects.all()
    context = {'advertisements':advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')