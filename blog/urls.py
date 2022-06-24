from django.urls import path

from .views import PostList, Create, PostDetailedView


urlpatterns = [

    path('', PostList.as_view(), name="home"),
    path('create/', Create.as_view(), name="create"),
    path('post/<int:pk>', PostDetailedView.as_view(), name="post_detail"),

    # path('blog_comments/<str:slug>/', PostDetail.as_view(),
    #      name="blog_comments"),
    
 ]
