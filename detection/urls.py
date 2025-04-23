from django.urls import path
from . import views

urlpatterns = [
    path('', views.detection_view, name='detection'),
]
