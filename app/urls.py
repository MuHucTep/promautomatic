from django.urls import include, path
from .views import *

urlpatterns = [
    path('', root_handler, name='root'),
]
