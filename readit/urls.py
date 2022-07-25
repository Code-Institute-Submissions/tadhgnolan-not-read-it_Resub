from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_posts, name='posts'),
    path('post/<int:id>/', views.view_post, name='view_post'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/update/<int:id>/', views.update_post, name='update_post'),
    path('posts/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('categories/', views.categories, name='categories'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/update/<int:id>/', views.update_category, name='update_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
]