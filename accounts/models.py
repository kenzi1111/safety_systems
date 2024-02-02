from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy


# djangoユーザマネージャーのカスタマイズ
class CustomUserManager(UserManager):
    # このカスタムマネージャを使用
    use_in_migrations = True

    # プロテクトメソッドの定義
    # メールとパスワードを受け取りユーザ情報に保存
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # 通常のユーザ作成
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    # 管理者作成
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# 認証と権限をつけたユーザモデルの作成
class User(AbstractBaseUser, PermissionsMixin):
    # ユーザ情報の保存用フィールド
    username = models.CharField(
        gettext_lazy("user name"),
        max_length=128,
        default="",
        blank=True,
    )
    email = models.EmailField(gettext_lazy("E-mail address"), unique=True)
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text=gettext_lazy(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        gettext_lazy("active"),
        default=True,
        help_text=gettext_lazy(
            "Designates whether this user should be treated as active."
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        gettext_lazy("date joined"), default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = gettext_lazy("user")
        verbose_name_plural = gettext_lazy("users")

    # コメントアウトしているのは古い記載＊昔のdjangoのもの
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.username or self.email

    # def __str__(self):
    #     return self.screen_name or self.email


# ユーザ情報ページ
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    user_image = models.ImageField(
        upload_to="profile_pictures/", blank=False, null=False
    )
