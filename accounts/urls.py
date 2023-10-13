from django.urls import path
from . import views
from .views import ShowMap
from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView, UserProfileDetailView


app_name = "accounts"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage.as_view(), name="logout"),
    path("profile/new/", UserProfileCreateView.as_view(), name="profile_Create"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/edit/", UserProfileUpdateView.as_view(), name="profile_update"),
    path("profile/<int:pk>/delete/",UserProfileDeleteView.as_view(),name="profile_delete",),
    path('showmap/<int:user_id>/', ShowMap.as_view(), name='show_map'),
]
