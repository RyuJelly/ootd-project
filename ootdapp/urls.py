from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.detail, name="detail"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('detail/<int:id>/<int:like>', views.detail, name="detail"),
    path('list/', views.list, name="list"),
]