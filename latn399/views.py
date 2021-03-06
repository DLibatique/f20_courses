from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import UserCourse
from django.contrib.auth.admin import User

# login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

course_context = {
    'course_number': 'LATN 399',
    'course_title': 'Roman Constructions of Gender and Sexuality',
    'content': 'hello world',
}

c = 'LATN399'

# Create your views here.
@login_required
def index(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Home'

        return render(request, 'latn399/index.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

@login_required
def resources(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Resources'

        return render(request, 'latn399/pages/resources.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})


@login_required
def policies(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Policies'

        return render(request, 'latn399/pages/policies.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})


@login_required
def grading(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Grading'

        return render(request, 'latn399/pages/grading.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})


@login_required
def liber(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Liber Personalis'

        return render(request, 'latn399/pages/liber.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})


@login_required
def schedule(request):

    if request.user.is_superuser or request.user.usercourse.course == c:

        course_context['page_title'] = 'Schedule'

        return render(request, 'latn399/pages/schedule.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})
