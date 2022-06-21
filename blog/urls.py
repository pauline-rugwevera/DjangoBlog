from django.urls import path

from .views import PostList

urlpatterns = [

    path('', PostList.as_view(), name="home"),
]

# from django.contrib import admin
# from django.urls import path, include


# urlpatterns = [
#   path('admin/', admin.site.urls),
#   path('', include('blog.urls')),
#   path('summernote/', include('django_summernote.urls')),
#   path('accounts/', include('allauth.urls')),
 
# ]