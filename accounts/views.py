import os
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserProfileForm
from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# from django.http import HttpRequest
from django.views import View

# from django.contrib.auth import get_user_model


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
    success_url = reverse_lazy("accounts:profile_list")

    # Userprofileのデータを新しいレコードに紐つけする
    def form_valid(self, form):
        user = self.request.user  # 現在のログインユーザーを取得
        form.instance.user = user  # UserProfileのインスタンスにユーザーをセット
        return super().form_valid(form)


# ユーザ情報の更新
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("accounts:profile_list")

    def form_valid(self, form):
        return super().form_valid(form)


# ユーザ情報の削除
class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "userprofile_conform_delete.html"
    success_url = reverse_lazy("accounts:profile_list")

    def delete(self, request, *args, **kwargs):
        # user = self.get_object()
        # user.save()
        return super().delete(request, *args, **kwargs)


# ユーザ情報の詳細閲覧
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "userprofile_detail.html"

    def get_object(self):
        user_id = self.kwargs.get("pk")  # URLから'pk'を取得します。
        # user__id=user_idを使用して、関連するUserのidに基づいてUserProfileを検索します。
        return get_object_or_404(UserProfile, user__id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 環境変数からAPIキーを取得してコンテキストに追加
        context["google_maps_api_key"] = os.getenv("GOOGLE_MAPS_API_KEY")
        return context


# ユーザ情報の一覧を表示
class UserProfileListView(ListView):
    model = UserProfile
    template_name = "profile_list.html"  # 一覧表示用のテンプレート名を指定
    context_object_name = "profiles"  # テンプレート内で使用する変数名を指定


# ユーザの住所情報を地図に表示
class ShowMap(View):
    def get(self, request, user_id):
        user_profile = UserProfile.objects.get(user_id=user_id)
        return render(request, "accounts/map.html", {"address": user_profile.address})
