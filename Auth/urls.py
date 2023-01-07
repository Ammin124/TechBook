from django.urls import path, include
from .views import UserRegisterView, UserEditView, ChangePass, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete
from django.contrib.auth import views as as_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('Register', UserRegisterView.as_view(), name='register'),
    path('EditProfile', UserEditView.as_view(), name='editProfile'),
    path('Password', ChangePass.as_view(), name='changePass'),
    path('reset-password/', PasswordReset.as_view(), name='password_reset'),
    path('reset-password-done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]
