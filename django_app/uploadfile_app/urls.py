from django.urls import path
from . import views

urlpatterns = [
    path('file/', views.MainView.as_view())
]