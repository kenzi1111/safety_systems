from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm


class Index(TemplateView):
    template_name = "accounts/index.html"


class LoginPage(LoginView):
    template_name = "accounts/login.html"


class LogoutPage(LogoutView):
    template_name = "accounts/index.html"


# ユーザ情報の新規投稿
class UserProfileCreateView(CreateView):
    models = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の更新
class UserProfileUpdateView(UpdateView):
    models = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の削除
class UserProfileDeleteView(DeleteView):
    models = UserProfile
    template_name = "userprofile_conform_delete.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の詳細閲覧
class UserProfileDetailView(DetailView):
    models = UserProfile
    template_name = "userprofile_detail.html"
