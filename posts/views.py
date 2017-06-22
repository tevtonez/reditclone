from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
  return render(request, 'posts/create_posts.html')
