from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dict = {'get_index':'Welcome to the views'}
    return render(request,'first_app/index.html',context = dict)
