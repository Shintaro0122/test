from django.shortcuts import render
from django.http import HttpResponse
#from django. import
#import requests
#import json


# Create your views here.
def index(request):
    return render(request,'mychannel/mychannel_info.html')
