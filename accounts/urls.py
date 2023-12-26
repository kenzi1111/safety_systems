from django.urls import path
from . import views
from .views import (
    UserProfileCreateView,
    UserProfileUpdateView,
    UserProfileDeleteView,
    UserProfileDetailView,
)


app_name = "accounts"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage.as_view(), name="logout"),
    path("profile/new/", views.UserProfileCreateView.as_view(), name="profile_create"),
    path(
        "profile/<int:pk>/",
        views.UserProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profile/<int:pk>/edit/",
        views.UserProfileUpdateView.as_view(),
        name="profile_update",
    ),
    path(
        "profile/<int:pk>/delete/",
        views.UserProfileDeleteView.as_view(),
        name="profile_delete",
    ),
    path("profile/", views.UserProfileListView.as_view(), name="profile_list"),
    # path("show_map/", views.ShowMap.as_view(), name="show_map"),
]
