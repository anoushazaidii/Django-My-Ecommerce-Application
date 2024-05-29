from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()  # Fetch all Product objects from the database
    return render(request,"shop/index.html",{'products': products})

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("productview")

def checkout(request):
    return HttpResponse("checkout")

def favorites(request):
    return HttpResponse("favorites")




