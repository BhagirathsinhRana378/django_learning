from django.shortcuts import render

# Create your views here.
def thor(request):
    return render(request, 'thor.html')