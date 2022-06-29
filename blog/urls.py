from django.urls import path
from .views import PostList, Create, PostDetailedView, UpdatePost


urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('create/', Create.as_view(), name="create"),
    path('post/<int:pk>/', PostDetailedView.as_view(), name="post-detail"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update-post"),



    # path('post/<int:pk>/comment/', AddComment.as_view(),
    #      name='add_comment'),
    # path('post/<int:pk>/comment/', AddComment.as_view(),
    #      name="add_comment"),

 
]
