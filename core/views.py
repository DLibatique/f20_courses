from django.shortcuts import render
from core.models import Course, Profile
from django.contrib.auth.admin import User
from django.contrib.auth.views import LoginView, LogoutView

# login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        clas199 = Course.objects.get(department='CLAS', course_number=199)
        latn213 = Course.objects.get(department='LATN', course_number=213)
        latn399 = Course.objects.get(department='LATN', course_number=399)

        if user:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                if user.is_superuser:
                    return render(request, 'core/superuser_access.html', {})
                else:
                    if user.profile.course == clas199:
                        return HttpResponseRedirect('CLAS199-F20/')
                    elif user.profile.course == latn213:
                        return HttpResponseRedirect('LATN213-F20/')
                    else:
                        return HttpResponseRedirect('LATN399-F20/')
        else:
            return render(request,'core/login.html', {'error': 'This username and password combination is incorrect!'})

    else:
        return render(request,'core/login.html', {})

class UserLogoutView(LogoutView):
    next_page = '/'

def no_access(request):
    return render(request, 'core/no_access.html', {})

def superuser_access(request):
    return render(request, 'core/superuser_access.html', {})
