from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('', views.PostlistView.as_view(), name='post_list'),
    path('<post_id>/share/', views.post_share, name='post_share'),

    # path('year/day/month/post', views.post_detail, name='post_detail'),
    #post views
    # path('', views.post_list, name='post_list'),
]