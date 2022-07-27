from django.urls import path
# from .views import PostList, Create, UpdatePost, DeletePost, UserEditView, EditProfileView
from .views import PostList, Create, UpdatePost, DeletePost, EditProfileView

from . import views


urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('create/', Create.as_view(), name="create"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('blog/<str:slug>/', views.post_detail, name="post-detail"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="delete-post"),
    path("search/", views.search, name="search"),
    path("register/", views.Register, name="register"),
    path("loginn/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),



    path("profile/", views.Profile, name="profile"),
    # path("edit_profile/", EditProfileView.as_view(), name="edit-profile"),
  
    path("<int:pk>/edit_profile/", EditProfileView.as_view(),
         name="edit-profile"),
         
    # path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
]
   
 
  


