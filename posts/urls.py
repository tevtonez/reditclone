from django.conf.urls import url
from . import views as posts_views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', posts_views.create, name = 'create'),
    url(r'^(?P<pk>[0-9]+)/upvote', posts_views.upvote, name = 'upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', posts_views.downvote, name = 'downvote'),
]
