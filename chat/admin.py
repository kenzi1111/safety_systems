from django.contrib import admin
from django.contrib import admin
from .models import Message

# メッセージがDBに登録されているか確認する
admin.site.register(Message)
