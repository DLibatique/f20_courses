from . import views

from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]
