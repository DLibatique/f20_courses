from django.urls import path, re_path
from . import views

app_name = 'latn399'

urlpatterns = [
    path('', views.index, name="index"),
    path('resources', views.resources, name="resources"),
    path('policies', views.policies, name="policies"),
    path('grading', views.grading, name="grading"),
    path('liber', views.liber, name="liber"),
    path('schedule', views.schedule, name="schedule"),
]
