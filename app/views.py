from django.shortcuts import render

def root_handler(request):
    return render(request, 'index.html')
