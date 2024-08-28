from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('contactus',views.contactus,name='contactus'),
    path('product',views.product,name='product'),
    path('brands',views.brands,name='brands'),
    path('blog',views.blog,name='blog'),
    path('aboutus',views.aboutus,name='aboutus')
]