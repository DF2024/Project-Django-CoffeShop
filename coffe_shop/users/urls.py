from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name="register")
]
