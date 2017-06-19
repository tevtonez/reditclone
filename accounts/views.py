from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):

  message = None

  if request.method == "POST":

    if request.POST['password1'] == request.POST['password2']:

      try:
        user = User.objects.get(username = request.POST['username'])
        message = "User already exists!"
        return render(request, 'accounts/signup.html', {
          'message' : message,})

      except User.DoesNotExist:

        try:
          user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
          login(request, user)

        except IntegrityError:
          message = "User hasn't been saved!"
          return render(request, 'accounts/signup.html', {
          'message' : message,})

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
