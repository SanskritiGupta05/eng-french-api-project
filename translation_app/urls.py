
from django.urls import path
from .views import index, translate

urlpatterns = [
    path('', index, name='index'),
    path('translate/', translate, name='translate'),
]
