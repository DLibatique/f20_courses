import clas199
import latn213
import latn399
from . import views

from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('CLAS199-F20/', include('clas199.urls')),
    path('LATN213-F20/', include('latn213.urls')),
    path('LATN399-F20/', include('latn399.urls')),
]
