from django.urls import path
from . import views

urlpatterns = [
    path("raport/", views.raport, name="raport"),
]