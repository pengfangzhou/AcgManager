from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    print "test()"
    return HttpResponse("Hello world!")

def index(request):
    return render(request,'index.html',{})

def info(request):
    return render(request,'info.html',{})

