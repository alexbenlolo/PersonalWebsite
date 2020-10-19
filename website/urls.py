from django.urls import path
from website import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]