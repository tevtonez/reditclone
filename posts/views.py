from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post

@login_required
def create(request):

  if request.method == 'POST':
    if request.POST['title'] and request.POST['url']:
      post = Post()
      post.title = request.POST['title']
      if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
        post.url = request.POST['url']
      else:
        post.url = 'http://' + request.POST['url']
      post.pub_date = timezone.datetime.now()
      post.author = request.user
      post.save()
      return redirect('home')
    else:
      message = "You have to provide both, a 'title' and a 'url'!"
      return render(request, 'posts/create_posts.html', {'message' : message,})
  else:
    return render(request, 'posts/create_posts.html')


def home(request):
  posts = Post.objects.order_by('rating')
  return render(request, 'posts/home.html',
    {
    'posts':posts,
    })
