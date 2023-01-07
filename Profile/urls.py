from django.urls import path
from . import views

urlpatterns = [
    path('img', views.profile_img, name='profile_img'),
    path('<str:auths>/', views.profile, name='profile'),
    path('Update/<int:pk>', views.UpdateProfile.as_view(), name='UpdateProfile'),
]
