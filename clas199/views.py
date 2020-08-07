from django.shortcuts import render
from django.views.generic import TemplateView

course_context = {
    'department': 'CLAS',
    'course_number': 199,
    'course_title': 'Intro to Greco-Roman Gender and Sexuality',
    'base_url': '/CLAS199-F20',
    'help': 'help',
}

# Create your views here.
class IndexView(TemplateView):

    template_name = 'clas199/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'

        # get course context
        for k in course_context:
            context[k] = course_context[k]

        return context

def resources(request):

    course_context['page_title'] = 'Resources'

    return render(request, 'clas199/resources.html', context=course_context)

def policies(request):

    course_context['page_title'] = 'Policies'

    return render(request, 'clas199/policies.html', context=course_context)

def grading(request):

    course_context['page_title'] = 'Grading'

    return render(request, 'clas199/grading.html', context=course_context)

def creative_projects(request):

    course_context['page_title'] = 'Creative Projects'

    return render(request, 'clas199/creative_projects.html', context=course_context)

def schedule(request):

    course_context['page_title'] = 'Schedule'

    return render(request, 'clas199/schedule.html', context=course_context)

def upload_portal(request):

    course_context['page_title'] = 'Upload Portal'

    return render(request, 'clas199/page.html', context=course_context)

def essay(request):

    course_context['page_title'] = 'Essay Tips'

    return render(request, 'clas199/essay.html', context=course_context)

def citations(request):

    course_context['page_title'] = 'Citation Examples'

    return render(request, 'clas199/citation.html', context=course_context)
