from django.urls import path

from AliMovie import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login.html', views.login, name="login"),
    path('signup.html', views.signup, name="signup"),
]
