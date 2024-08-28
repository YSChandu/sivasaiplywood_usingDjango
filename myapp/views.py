from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'home.html')


def services(request):
    return render(request,'services.html')


def product(request):
    return render(request,'product.html')


def contactus(request):
    return render(request,'contactus.html')


def brands(request):
    return render(request,'brands.html')


def blog(request):
    return render(request,'blog.html')


def aboutus(request):
    return render(request,'aboutus.html')
