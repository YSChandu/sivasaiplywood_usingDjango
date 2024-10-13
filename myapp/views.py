from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    brands =["kitply","century","bluestar","austin","chandu"]
    products=["product1","product1","product1","product1","product1","product1","product1","product1"]
    context={'products':products,'brands':brands}
    return render(request,'home.html',context)


def services(request):
    return render(request,'services.html')


def product(request):
    products=["product1","product2","product3","product4","product5","product6","product7","product8","product9"]
    return render(request,'product.html',{'products':products})


def contactus(request):
    return render(request,'contactus.html')


def brands(request):
    return render(request,'brands.html')


def blog(request):
    return render(request,'blog.html')


def aboutus(request):
    return render(request,'aboutus.html')
