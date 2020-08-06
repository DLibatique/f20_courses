from django.urls import path, re_path
from . import views

app_name = 'latn399'

urlpatterns = [
    path('', views.index, name="index"),
]
