from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'about/about.html')

def who_we_are(request):
    return render(request, 'about/who_we_are.html')

def what_we_do(request):
    return render(request, 'about/what_we_do.html')

def get_in_touch(request):
    return render(request, 'about/get_in_touch.html')
