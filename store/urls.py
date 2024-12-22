from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
]