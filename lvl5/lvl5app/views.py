from django.shortcuts import render
from lvl5app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'logout.html')

def register(request):
    registered = False
    if request.method == "POST":
        User_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if User_form.is_valid() and profile_form.is_valid():
            user = User_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(User_form.errors,profile_form.errors)
    else:
         User_form = UserForm()
         profile_form = UserProfileInfoForm()
    return render(request,'registration.html',{'user_form':User_form,'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("username{} and password {}".format(username,password))
            return HttpResponse("invlaid login details")
    else:
        return render(request,'login.html',{})