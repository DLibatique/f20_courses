from django.shortcuts import render

course_context = {
    'course_number': 'CLAS 199',
    'course_title': 'Intro to Greco-Roman Gender and Sexuality',
    'base_url': '/CLAS199-F20',
    'help': 'help',
}

# Create your views here.
def index(request):

    course_context['page_title'] = 'Home'

    return render(request, 'clas199/index.html', context=course_context)

def resources(request):

    course_context['page_title'] = 'Resources'

    return render(request, 'clas199/resources.html', context=course_context)

def policies(request):

    course_context['page_title'] = 'Policies'

    return render(request, 'clas199/page.html', context=course_context)

def grading(request):

    course_context['page_title'] = 'Grading'

    return render(request, 'clas199/page.html', context=course_context)

def creative_projects(request):

    course_context['page_title'] = 'Creative Projects'

    return render(request, 'clas199/page.html', context=course_context)

def schedule(request):

    course_context['page_title'] = 'Schedule'

    return render(request, 'clas199/page.html', context=course_context)

def upload_portal(request):

    course_context['page_title'] = 'Upload Portal'

    return render(request, 'clas199/page.html', context=course_context)
