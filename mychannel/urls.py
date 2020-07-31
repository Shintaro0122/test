from django.urls import path
from . import views

app_name = 'mychannel'
urlpatterns = [
 path('', views.index, name='index'),
]
