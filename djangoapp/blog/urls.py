
from django.urls import path
from blog.views import index, post, page

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/', index, name='post'),
    path('page/', index, name='page'),
]

