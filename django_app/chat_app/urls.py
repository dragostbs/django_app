from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('chat/', views.MainView.as_view(), name='main')
]