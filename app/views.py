from django.shortcuts import render, get_object_or_404
from .models import Project

def root_handler(request):
    projects = Project.objects.filter(is_active=True)
    return render(request, 'index.html', {'projects': projects})

def projects_list(request):
    projects = Project.objects.filter(is_active=True)
    return render(request, 'index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_active=True)
    return render(request, 'projects/project_detail.html', {'project': project})

def page_not_found(request, exeption):
    return render(request, '404.html', status=404)
