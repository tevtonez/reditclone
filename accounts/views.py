from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



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
      return render(request, 'accounts/signup.html', {'message' : message,})

  else:
    return render(request, 'accounts/signup.html')



def usrlogin(request):

  message = None

  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)

    if user is not None:
      login(request, user)

      # redirect users from @login_required views
      if 'next' in request.POST:
        return redirect(request.POST["next"])

      message = "Logged in successfull!"
      return render(request, 'accounts/login.html', {'message' : message,})
    else:
      message = "The user name and password didn't match."
      return render(request, 'accounts/login.html', {'message' : message,})
  else:
    return render(request, 'accounts/login.html')

