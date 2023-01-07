
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('datels/<int:pk>', views.DetailsView.as_view(), name='details'),
    path('Add Post/', views.AddPostView.as_view(), name='addPost'),
    path('UpdatePost/<int:pk>', views.UpdatePostView.as_view(), name='updatePost'),
    path('DedetePost/<int:pk>', views.DeletePostView.as_view(), name='deletePost'),
    path('About', views.about, name='about'),
    path('Contact', views.contact, name='contact'),
    path('category/<str:cats>', views.categoryView, name='category'),
    path('like/<int:pk>', views.likesPost, name='likePost'),
    path('search/', views.search, name='search'),
    path('postComment/', views.postComment, name='postComment'),

]
