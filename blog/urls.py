from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.login, name='signup'),
]