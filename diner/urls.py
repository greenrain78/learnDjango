from django.urls import path, include
from diner import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('', views.bootstrap, name='bootstrap'),

]
