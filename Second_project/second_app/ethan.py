from django.shortcuts import render
from django.http import HttpResponse

def mission(request):
    dict1 = {'ehunt':"Your Mission if you choose to accept"}
    return render(request,'eindex.html',context= "ehunt")
