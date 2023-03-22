from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
<<<<<<< HEAD
    path('posts/<ind:post_id>/edit/', views.post_edit, name='edit'),
=======
    path('posts/<int:post_id>/edit/', views.post_edit, name='edit'),
>>>>>>> e7a16aafb5fab4be21e96d5025c41823107c6b6b
    path('create/', views.post_create, name='create'),
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
