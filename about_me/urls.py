from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_me_index, name="about_me"),
]
