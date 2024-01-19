from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models, forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Message, MessageRead
from django.utils import timezone
from datetime import timedelta
from django.db.models import Max, F


User = get_user_model()


class Index(LoginRequiredMixin, ListView):
    model = models.Room
    template_name = "chat/index.html"
    context_object_name = "rooms"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = forms.SearchForm(self.request.GET or None)
        keywords = form.get_keywords()

        # queryset.filter(user=self.request.user, keywords=keywords) の代わりに
        return queryset.filtering(user=self.request.user, keywords=keywords)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = forms.SearchForm(self.request.GET or None)

        return context


class CreateRoom(LoginRequiredMixin, CreateView):
    model = models.Room
    template_name = "chat/room_form.html"
    form_class = forms.RoomForm
    success_url = reverse_lazy("chat:index")

    def form_valid(self, form):
        form.instance.set_host(self.request.user)

        return super().form_valid(form)


class OnlyRoomHostMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        room = self.get_object()
        return room.is_host(self.request.user)


class UpdateRoom(LoginRequiredMixin, OnlyRoomHostMixin, UpdateView):
    model = models.Room
    template_name = "chat/room_form.html"
    form_class = forms.RoomForm
    success_url = reverse_lazy("chat:index")


class DeleteRoom(LoginRequiredMixin, OnlyRoomHostMixin, DeleteView):
    model = models.Room
    success_url = reverse_lazy("chat:index")

    def get(self, request, *args, **kwargs):
        # ignore direct access
        return self.handle_no_permission()


class OnlyAssignedUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        room = self.get_object()

        return room.is_assigned(self.request.user)


class EnterRoom(LoginRequiredMixin, OnlyAssignedUserMixin, DetailView):
    model = models.Room
    template_name = "chat/chat_room.html"
    context_object_name = "room"


# メッセージの未読ユーザand既読ボタン未クリックユーザのリスト作成
# class UnreadListView(ListView):
#     model = Message
#     template_name = "chat/unread_list.html"

#     def get_queryset(self):
#         cutoff_time = timezone.now() - timedelta(hours=48)

#         latest_messages_dates = Message.objects.values("room").annotate(
#             latest_date=Max("created_at")
#         )

#         latest_messages = Message.objects.filter(
#             created_at__in=latest_messages_dates.values("latest_date")
#         )

#         unread_messages = latest_messages.filter(
#             Q(reads__isnull=True) | Q(reads__read_at__lt=cutoff_time)
#                 ).distinct()

#         return unread_messages


class UnreadListView(ListView):
    model = User  # 未返信ユーザーのリストを表示するためにUserモデルを使用
    template_name = "chat/unread_list.html"

    def get_queryset(self):
        cutoff_time = timezone.now() - timedelta(hours=48)

        latest_messages_dates = Message.objects.values("room").annotate(
            latest_date=Max("created_at")
        )
        latest_messages = Message.objects.filter(
            created_at__in=latest_messages_dates.values("latest_date"),
            owner=F("room__host"),  # ルームのホストが送信したメッセージのみを対象とする
        )

        unread_users = User.objects.filter(
            rooms__messages__in=latest_messages
            ).exclude(
            id__in=MessageRead.objects.filter(
            message__in=latest_messages, read_at__gte=cutoff_time
            ).values("reader_id")
        )
        
        return unread_users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["unread_users"] = self.get_queryset()
        return context


# 既読ボタンの処理
def mark_message_as_read(request, message_id):
    # 既読ボタンがクリックされたメッセージを取得
    message = get_object_or_404(Message, id=message_id)

    # 既読情報を記録
    MessageRead.objects.get_or_create(message=message, reader=request.user)

    # 成功レスポンスを返す
    return JsonResponse({"status": "success"})
