from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   #path("",views.MyModelView.as_view()),
   path('login/',views.login,name="account_login"),
	#path('logout/',views.logout,name="account_logout"),
   path('Dashboard/',views.dashboard,name="dashboard"),
   path('Profile/',views.profile,name="profile")
	
    
]