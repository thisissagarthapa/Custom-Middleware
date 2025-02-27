from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home_1(request):
    a/10 
    print(a/10)
    return HttpResponse("This is home page")

def home(request):
    context={
        "name":"sagar",
           "age": 22
    }
    return TemplateResponse(request,'home.html',context)
