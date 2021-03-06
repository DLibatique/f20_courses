from django.urls import path, re_path
from . import views

app_name = 'clas199'

urlpatterns = [
    path('', views.index, name="index"),
    path('resources', views.resources, name="resources"),
    path('policies', views.policies, name="policies"),
    path('grading', views.grading, name="grading"),
    path('creative_projects', views.creative_projects, name="creative_projects"),
    path('schedule', views.schedule, name="schedule"),
    path('essay', views.essay, name="essay"),
    path('citations', views.citations, name="citations"),
]
