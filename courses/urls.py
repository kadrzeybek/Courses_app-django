from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa',views.home),
]