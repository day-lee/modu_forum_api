from django.urls import path
from .views import PostList, PostSearch
from . import views

app_name = 'modu_forum_api'

urlpatterns = [
                path('', PostList.as_view(), name='postlist'),
                path('search/', PostSearch.as_view(), name='postsearch'),
                path('comment/<int:pk>/', views.CommentList, name='commentlist'),
                path('create-post', views.create_post, name='postcreate'),
                path('edit/<int:pk>/', views.update_post, name='postupdate'),
                path('delete/<int:pk>/', views.delete_post, name='postdelete'),
                path('create-comment/<int:pk>/', views.create_comment, name='commentcreate'),
]
