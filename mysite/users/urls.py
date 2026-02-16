from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView, name="logout"),
    path("dashboard/", views.DashboardView, name="dashboard"),
]
