from django.urls import path
from django.urls.resolvers import URLPattern
from .views import blog_view

urlpatterns: list[URLPattern] = [
    path('blog/', blog_view, name='blog'),
]
