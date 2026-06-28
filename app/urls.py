from django.urls import include, path
from .views import *

urlpatterns = [
    path('', root_handler, name='root'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
]
