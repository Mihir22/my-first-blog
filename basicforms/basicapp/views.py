from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'baiscapp/index.html')

def form_name_view(request):
    form = forms.form_name()
    if request.method =='POST':
        form = forms.form_name(request.POST)

        if form.is_valid() :
            print("validation success")
            print("NAME: ",  form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])




    return render(request,'baiscapp/form_page.html',{'form':form})
