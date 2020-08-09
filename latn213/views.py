from django.shortcuts import render

course_context = {
    'course_number': 'LATN 213',
    'course_title': 'Intermediate Latin 1',
    'content': 'hello world',
}

# Create your views here.
def index(request):

    return render(request, 'latn213/index.html', context=course_context)
