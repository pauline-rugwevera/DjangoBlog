from django.urls import path
from .views import PostList, UpdatePost, Create, DeletePost
from . import views


urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('create/', Create.as_view(), name="create"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="delete-post"),
    path('blog/<str:slug>/', views.post_detail, name="post-detail"),
    path("search/", views.search, name="search"),
    path("profile/", views.profile, name="profile"),
  
]
