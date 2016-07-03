from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

def sign_in(request):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    
    user = authenticate(username=username, password=password)
    message = None
    if user is not None:
        if user.is_active:
            login(request, user)
            message = 'success'
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            message = 'disabled account'

    else:
        # Return an 'invalid login' error message.
        message = 'invalid login'

    template = loader.get_template('user/login.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))

