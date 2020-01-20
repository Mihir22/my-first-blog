from django.shortcuts import render
from django.http import HttpResponse
from .forms import form_name

# Create your views here.
def index(request):
    dict = {'get_index':'Mission not available'}
    return render(request,'index.html',context = dict)

def form_name_view(request):
    form = form_name(request.post)
    return render(request,'eindex.html',{'form':form})
