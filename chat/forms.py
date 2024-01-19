from django import forms
from django.utils.translation import gettext_lazy
from . import models
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()


class SearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy("keywords (split space)"),
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": gettext_lazy("チャットルームの名前を入力してください"),
                "class": "form-control",
            }
        ),
    )

    def get_keywords(self):
        init_keywords = ""
        keywords = init_keywords

        if self.is_valid():
            keywords = self.cleaned_data.get("keywords", init_keywords)

        return keywords


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ("name", "description", "participants")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": gettext_lazy("チャットルームの名前を入力してください"),
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "cols": 10,
                    "style": "resize: none",
                    "placeholder": gettext_lazy("チャットルームの概要"),
                    "class": "form-control",
                }
            ),
            "participants": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["participants"].queryset = User.objects.filter(is_staff=False)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]  # メッセージの内容のみをユーザーに入力させる

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget = forms.Textarea(
            attrs={"placeholder": "メッセージを入力"}
        )
