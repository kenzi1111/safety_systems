from django import forms
from .models import User, UserProfile


# ユーザ情報のCRUD機能
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["address", "phone_number", "user_image"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]  # User モデルの username,email を扱う
