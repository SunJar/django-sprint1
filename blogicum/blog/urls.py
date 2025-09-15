from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main_page_view, name='index'),
    path('posts/<int:post_id>/', views.details_of_posts, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_view,
        name='category_posts',
    ),
]
