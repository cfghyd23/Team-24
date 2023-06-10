from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout,login as user_login
from django.contrib.auth.models import User
from .forms import ProfileEditForm,UserProfileEditForm
#from rest_framework import APIView



#class MyModelView(APIView):
 #   def post(self, request):
  #      serializer = MyModelSerializer(data=request.data)
   #     if serializer.is_valid():
    #        serializer.save()  # Save the validated data to the database
     #       return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#login view

@login
def dashboard(request):
	if request.user.is_staff:
		return render(request,'dashboard.html',{'interns':User.objects.filter(is_staff = False),'total_interns':User.objects.filter(is_staff = False).count()})
	else:
		return redirect('account_profile',username=request.user.username)
	

@login
def profile(request,username):
	return render(request,'profile.html',{'userdata':User.objects.get(username=username)})

@login
def edit_profile(request,username):
	if request.method == "POST":
		form = ProfileEditForm(request.POST,instance=request.user)
		profile_form = UserProfileEditForm(request.POST, request.FILES,instance = request.user.profile)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			return redirect('account_profile',username=username)
	else:
		form = ProfileEditForm(instance=request.user)
		profile_form = UserProfileEditForm(instance = request.user.profile)
	return render(request,'profile/edit_profile.html',{'form':form,'profile':profile_form})


# Create your views here.




