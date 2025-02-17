from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name='home'),
    path("todos/", views.todos, name='todos'),
    path("aboutus/", views.aboutus, name='about'),
]
