from django.shortcuts import render
from django.views.generic import TemplateView

# login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from core.models import UserCourse
from django.contrib.auth.admin import User

course_context = {
    'department': 'CLAS',
    'course_number': 199,
    'course_title': 'Intro to Greco-Roman Gender and Sexuality',
    'base_url': '/CLAS199-F20',
    'help': 'help',
}

c = 'CLAS199'

# Create your views here.
@login_required
def index(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Home'

        return render(request, 'clas199/index.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def resources(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Resources'

        return render(request, 'clas199/pages/resources.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def policies(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Policies'

        return render(request, 'clas199/pages/policies.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def grading(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Grading'

        return render(request, 'clas199/pages/grading.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def creative_projects(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Creative Projects'

        return render(request, 'clas199/pages/creative_projects.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def schedule(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Schedule'

        return render(request, 'clas199/pages/schedule.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def essay(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Essay Tips'

        return render(request, 'clas199/pages/essay.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def citations(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Citation Examples'

        return render(request, 'clas199/pages/citation.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})
