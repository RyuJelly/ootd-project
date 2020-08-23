from django.urls import path
from . import views

urlpatterns = [
    path('photo/<int:id>/', views.photo, name="photo"),
    path('list/', views.list, name="list"),
]