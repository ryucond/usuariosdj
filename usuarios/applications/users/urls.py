from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name='add-user'),
    path("login/", views.LoginUser.as_view(), name='login-user'),
    path("logout/", views.LogoutUser.as_view(), name='logout-user'),
    path("update/", views.UpdatePassword.as_view(), name='update-user'),
    path("verify/<pk>/", views.CodeVerificationView.as_view(), name='verify-user'),
]