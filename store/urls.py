from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('login/', views.Login_User, name="login"),
    path('logout/', views.Logout_User, name="logout"),
    path('register/', views.Register_User, name="register")
]