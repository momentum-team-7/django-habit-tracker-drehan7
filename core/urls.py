from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_page, name="home_page"),
    path('create_profile/', views.create_profile, name="create_profile"),
]