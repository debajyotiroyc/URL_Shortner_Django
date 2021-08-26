from django.contrib import admin
from django.urls import path,include
from shortener import views
urlpatterns = [
    path('', views.index,name='index'),
    path('create', views.create,name='create'),
    path('<str:pk>', views.go,name='go'),
]
