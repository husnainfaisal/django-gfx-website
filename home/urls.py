from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("logos", views.logos, name='logos'),
   path("brandinglogos", views.brandinglogos, name='brandinglogos'),
   path("banners", views.banners, name='banners'),
   path("overlays", views.overlays, name='overlays'),
   path("animations", views.animations, name='animations'),
   path("pricing", views.pricing, name='pricing'),
   path("contactus", views.contactus, name='contactus'),
]

