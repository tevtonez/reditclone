from django.conf.urls import url
from . import views as posts_views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', posts_views.create, name = 'create'),
]
