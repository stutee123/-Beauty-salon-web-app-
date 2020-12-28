from django.urls import path,include
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('blogs/',views.blogs,name='blogs'),
    path('fullservices/', views.fullServices,name='fullservices'),
    path('fullblogs/<str:blog_id>/', views.fullBlogs,name='fullblogs'),
    path('haircare/', views.haircare,name='haircare'),
    path('makeupservice/', views.makeupservice, name='makeupservice'),
    path('facialtreatment/', views.facialtreatment, name='facialtreatment'),
    path('nailart/', views.nailart, name='nailart'),
    path('hairstyle/',views.hairstyle, name='hairstyle'),
    path('pedicure/', views.pedicure, name='pedicure'),
    path('manicure/', views.manicure, name='manicure'),
    
    ]
