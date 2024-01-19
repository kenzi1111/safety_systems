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
from .forms import UserProfileForm, UserForm  # screen_nameを使用するため追加
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.http import HttpResponseRedirect

# 未読メッセージのバッチ処理
# from django.utils import timezone
# from datetime import timedelta
# from chat.models import Message, RoomParticipant, MessageRecipient


# from .utilities import get_coordinates_for_address

# from django.http import HttpRequest
# from django.views import View

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

    # コンテキストデータの取得
    # コンテキストデータの生成
    def get_context_data(self, **kwargs):
        # コンテキストデータの取得
        context = super().get_context_data(**kwargs)
        # POSTされたデータの受け取り先の作成（formの初期化）
        if "user_form" not in context:
            context["user_form"] = UserForm(self.request.POST or None)
        if "form" not in context:
            context["form"] = UserProfileForm(self.request.POST or None)
        return context

    # POSTされたデータの検証
    def form_valid(self, form):
        user_form = UserForm(self.request.POST)
        profile_form = UserProfileForm(self.request.POST, self.request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


# ユーザ情報の更新
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "userprofile_form.html"
    success_url = reverse_lazy("accounts:profile_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        if not context.get("user_form"):
            context["user_form"] = UserForm(instance=user_profile.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        user_form = UserForm(request.POST, instance=self.object.user)

        if form.is_valid() and user_form.is_valid():
            return self.form_valid(form, user_form)
        else:
            return self.form_invalid(form, user_form)

    def form_valid(self, form, user_form):
        # User インスタンスを保存
        user = user_form.save()
        # UserProfile インスタンスの user フィールドを更新
        user_profile = form.save(commit=False)
        user_profile.user = user
        user_profile.save()
        return HttpResponseRedirect(self.get_success_url())


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
        return get_object_or_404(UserProfile, user_id=user_id)

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


