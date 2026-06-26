from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello, YOur at the page")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("hiii, YOur at about the page")
    return render(request, 'website/index2.html')

def contact(request):
    return HttpResponse("hello, YOur at contact the page")