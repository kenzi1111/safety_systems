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
from django.shortcuts import render,get_object_or_404
from .models import UserProfile
from django.http import HttpRequest
from django.views import View
from django.contrib.auth import get_user_model

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


# ユーザ情報の更新
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("accounts:profile_list")


# ユーザ情報の削除
class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "userprofile_confirm_delete.html"
    success_url = reverse_lazy("accounts:profile_list")

    def delete(self, request, *args, **kwargs):
        user_profile = self.get_object()
        user = get_object_or_404(get_user_model(), email=user_profile.user.email)
        # ここでuserに対しての追加の操作を実行します。
        # 例: user.delete() または user.is_active = False followed by user.save()
        
        # Userモデルのインスタンスに対する操作の後に、UserProfileインスタンスを削除します。
        response = super().delete(request, *args, **kwargs)
        return response
        


# ユーザ情報の詳細閲覧
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "userprofile_detail.html"

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
