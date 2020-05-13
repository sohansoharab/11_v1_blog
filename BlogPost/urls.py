from django.urls import path
from BlogPost import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('newpost', views.CreatePost.as_view(), name='newpost'),
    path('post_details/<int:pk>', views.PostDetails.as_view(), name='post_detail'),
    path('post_details/<int:pk>/edit', views.UpdatePost.as_view(), name='post_update'),
    path('post_details/<int:pk>/delete', views.DeletePost.as_view(), name='post_delete'),

]
