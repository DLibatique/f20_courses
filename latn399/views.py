from django.shortcuts import render
from django.views.generic import TemplateView

course_context = {
    'course_number': 'LATN 399',
    'course_title': 'Roman Constructions of Gender and Sexuality',
    'content': 'hello world',
}

# Create your views here.
class IndexView(TemplateView):

    template_name = 'latn399/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home'

        # get course context
        for k in course_context:
            context[k] = course_context[k]

        return context

def resources(request):

    course_context['page_title'] = 'Resources'

    return render(request, 'latn399/pages/resources.html', context=course_context)

def policies(request):

    course_context['page_title'] = 'Policies'

    return render(request, 'latn399/pages/policies.html', context=course_context)

def grading(request):

    course_context['page_title'] = 'Grading'

    return render(request, 'latn399/pages/grading.html', context=course_context)

def assignments(request):

    course_context['page_title'] = 'Assignments'

    return render(request, 'latn399/pages/assignments.html', context=course_context)

def schedule(request):

    course_context['page_title'] = 'Schedule'

    return render(request, 'latn399/pages/schedule.html', context=course_context)
