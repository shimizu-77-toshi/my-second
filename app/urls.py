from django.urls import path
from . import views

urlpatterns = [
      path("", views.index, name = "TOM"),
      path("form", views.form, name = "form"),
]