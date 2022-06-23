from django.urls import path

from .views import PostList, Create


urlpatterns = [

    path('', PostList.as_view(), name="home"),
    path('create/', Create.as_view(), name="create"),

    # path('blog_comments/<str:slug>/', PostDetail.as_view(),
    #      name="blog_comments"),
    
 ]
