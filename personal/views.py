from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def bootstrap(request):
    return render(request, 'bootstrap.html')

def inndexx(request):
    return render(request, 'inndexx.html')


# Create your views here.