from django.urls import path
from django.urls.resolvers import URLPattern
from .views import blog_view, post_detail_view

urlpatterns: list[URLPattern] = [
    path('blog/', blog_view, name='blog'),
    path('blog/<int:post_id>/', post_detail_view, name='post_detail'),
]
