from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.MyModelView.as_view()),
   path('login/',LoginView.as_view(),name="account_login"),
	path('logout/',views.logout,name="account_logout"),
	path('register/',views.register,name="internRegister"),
    
]