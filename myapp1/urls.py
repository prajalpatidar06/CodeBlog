from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about , name='about'),
    path('register', views.user_register , name='user_register'),
    path('_login', views.user_login, name='user_login'),
]
