from django.contrib import admin
from django.urls import path
from . import views
from . feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<post_id>/share/', views.post_share, name='post_share'),
    path('', views.post_list, name='post_list'),
    #feeds
    path('feed/', LatestPostsFeed(), name='post_feed'),
    #search
    path('search/', views.post_search, name='post_search'),
]
    # path('', views.PostlistView.as_view(), name='post_list'),
    # path('year/day/month/post', views.post_detail, name='post_detail'),
    #post views
    