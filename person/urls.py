from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', list_person),
]