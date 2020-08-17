from django.shortcuts import render
from django.views.generic import TemplateView

# login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from core.models import Course, Profile
from django.contrib.auth.admin import User

course_context = {
    'course_number': 'LATN 213',
    'course_title': 'Intermediate Latin 1',
    'content': 'hello world',
}

c = Course.objects.get(course_number=213)

# Create your views here.
@login_required
def index(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Home'

        return render(request, 'latn213/index.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})


def resources(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Resources'

        return render(request, 'latn213/pages/resources.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

def policies(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Policies'

        return render(request, 'latn213/pages/policies.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

def grading(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Grading'

        return render(request, 'latn213/pages/grading.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

def assignments(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Assignments'

        return render(request, 'latn213/pages/assignments.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

def schedule(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Schedule'

        return render(request, 'latn213/pages/schedule.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})

def grammar(request):

    if request.user.is_superuser or request.user.profile.course == c:

        course_context['page_title'] = 'Running Grammar'

        return render(request, 'latn213/pages/grammar.html', context=course_context)

    else:

        return render(request, 'core/no_access.html', {})
