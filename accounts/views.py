from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signup(request):

  message = None

  if request.method == "POST":
    if request.POST['password1'] == request.POST['password2']:
      try:
        User.objects.create_user(request.POST['username'], password = request.POST['password1'])
      except IntegrityError:
        status = 'user already exists'
      else:
        message = "Congratulations, you've just signed up!"
        return render(request, 'accounts/signup.html', {
        'message' : message,
      })
    else:
      message = "Passwords didn't match!"
      return render(request, 'accounts/signup.html', {
        'message' : message,
      })
  else:
    return render(request, 'accounts/signup.html')
