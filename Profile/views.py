from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy

from App.models import Post
from .models import Profile
from django.views.generic import UpdateView
from .forms import EditProfileForms
# Create your views here.

def profile(request, auths):
    posts = Post.objects.filter(author= auths)
    #post = Post.objects.get()
    context = {
        'posts': posts,
    }
    return render(request, 'profile/profile.html',context)

def profile_img(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html',context)

class UpdateProfile(UpdateView):
    model = Profile
    form_class = EditProfileForms
    template_name = 'profile/UpdateUserProfile.html'
    success_url = reverse_lazy('index')