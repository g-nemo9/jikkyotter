from django.urls import path
from . import views


app_name = 'jikkyotter'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/create/', views.CreatePost.as_view(), name='post_create'),
    path('post/detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('user/detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('post/tags/<str:tag_name>/', views.TagList.as_view(), name='post_tags'),
]
