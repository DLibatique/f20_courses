from django.shortcuts import render

course_context = {
    'course_number': 'LATN 399',
    'course_title': 'Roman Constructions of Gender and Sexuality',
    'content': 'hello world',
}

# Create your views here.
def index(request):

    return render(request, 'index.html', context=course_context)
