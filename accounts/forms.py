from django import forms
from .models import User, UserProfile
from django.contrib.auth import get_user_model


# ユーザ情報のCRUD機能
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["address", "phone_number", "user_image"]


class UserForm(forms.ModelForm):
    email = forms.ChoiceField(choices=[])  # 初期状態では空の選択肢

    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # UserProfile に紐付いているユーザのEmailリストを取得
        used_emails = UserProfile.objects.values_list('user__email', flat=True)
        # UserProfile に紐付いていないユーザのEmailだけを取得
        available_emails = get_user_model().objects.exclude(email__in=used_emails)
        self.fields['email'].choices = [(user.email, user.email) for user in available_emails]