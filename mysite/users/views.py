from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import RegisterForm


def LogoutView(request):
    logout(request)
    return redirect("users:login")


@login_required(login_url="login")
def DashboardView(request):
    user = request.user
    return render(request, "users/dashboard.html", {"user": user})


class UserLoginView(LoginView):
    template_name = "users/login.html"

    """
    dispatch() est appelée avant get() et post()
    donc :
    si user connecté → redirect immédiate
    sinon → Django continue le flow normal du login
    """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("users:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = AuthenticationForm()
        return render(request, str(self.template_name), {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:dashboard")
        return render(request, str(self.template_name), {"form": form})


class UserRegisterView(CreateView):
    template_name = "users/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("users:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = RegisterForm()
        return render(request, str(self.template_name), {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:dashboard")
        return render(request, str(self.template_name), {"form": form})
