from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpFrom

class ChangePass(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/changePas.html'
    success_url = reverse_lazy('index')


class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

class UserRegisterView(CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class PasswordReset(PasswordResetView):
    template_name = 'registration/passwordReset.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
