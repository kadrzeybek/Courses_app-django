from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('homepage',views.home),
    path('contact',views.contact),
    path('about',views.aboutUs),
]
