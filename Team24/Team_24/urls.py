from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('login/', views.loginListView.as_view()),
  path('login/<int:id>/', views.loginListView.as_view()),
]