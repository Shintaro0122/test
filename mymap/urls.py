from django.urls import path
from . import views

app_name = 'mymap'
urlpatterns = [
 path('', views.index, name='index'),
]
