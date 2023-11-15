from django import forms
from .models import UserProfile


# ユーザ情報のCRUD機能
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user", "username", "address", "phone_number", "user_image"]
