from django.contrib import admin
from django.urls import path
from .views import HomePage

urlpatterns = [
    path("login", HomePage.as_view(), name='home')
]