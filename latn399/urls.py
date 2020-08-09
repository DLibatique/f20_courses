from django.urls import path, re_path
from . import views

app_name = 'latn399'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('resources', views.resources, name="resources"),
    path('policies', views.policies, name="policies"),
    path('grading', views.grading, name="grading"),
    path('assignments', views.assignments, name="assignments"),
    path('schedule', views.schedule, name="schedule"),
]
