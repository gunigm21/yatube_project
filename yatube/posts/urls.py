from django.urls import path
from . import views

app_name = 'posts_detail'

urlpatterns = [
    path('', views.index, name='main'),
    path('group/<slug:slug>/', views.group_posts, name='posts_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('create/', views.post_create, name='post_create'),
    path(
        'posts/<int:post_id>/comment/', views.add_comment, name='add_comment'
    ),
    path(
        'posts/comments/<int:comment_id>/delete/',
        views.comment_delete, name='delete_comment'
    ),
    path('follow/', views.follow_index, name='follow_index'),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name="profile_unfollow"
    ),
] 
