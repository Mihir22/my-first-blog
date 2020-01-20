from django.shortcuts import render
from django.http import HttpResponse
from dbase.models import user
from dbase.forms import user_info
# Create your views here.

def index(request):
    return render(request,"db_app/main.html")

def user(request):

    form = user_info()

    if request.method == "POST":
        form = user_info(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error")

    return render(request,'db_app/index.html',{'form':form})
