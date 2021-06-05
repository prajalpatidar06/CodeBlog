from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about , name='about'),
    path('register', views.user_register , name='register'),
    path('_login', views.user_login, name='_login'),
    path('logout', views.user_logout, name='logut'),
]
