from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

# Create your views here.
def index(request):
    allProds = []
    catProds = Product.objects.values("product_category","id")
    cats = {item['product_category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(product_category = cat)
        n = len(prod)
        nSlides = n//4 + math.ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
        
    params= {"allProds":allProds}
    return render(request, 'shop/indexV2.html',params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return render(request,"shop/contactus.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productView(request,myid):
    product = Product.objects.filter(id=myid)
    print(product,myid)

    return render(request,"shop/prodview.html",{'product':product[0]})

def checkout(request):
    return render(request,"shop/checkout.html")

def favorites(request):
    return render(request,"shop/favorites.html")




