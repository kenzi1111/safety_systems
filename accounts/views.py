from django.views.generic import (TemplateView, CreateView, UpdateView, DeleteView, DetailView,)
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserProfileForm
from django.shortcuts import render
from .models import UserProfile
from django.http import HttpRequest
from django.views import View


class Index(TemplateView):
    template_name = "accounts/index.html"


class LoginPage(LoginView):
    template_name = "accounts/login.html"


class LogoutPage(LogoutView):
    template_name = "accounts/index.html"


# ユーザ情報の新規投稿
class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の更新
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の削除
class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "userprofile_conform_delete.html"
    success_url = reverse_lazy("profile_list")


# ユーザ情報の詳細閲覧
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "userprofile_detail.html"

# ユーザの住所情報を地図に表示
class ShowMap(View):
    def get(self, request, user_id):
        user_profile = UserProfile.objects.get(user_id=user_id)
        return render(request, "accounts/map.html", {"address": user_profile.address})