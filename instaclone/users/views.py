from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .form import UserSignUpForm

# Create your views here.

def index(request):
    # message = f"{request.method} -----> {request.path_info}"

    # message = "I don't know about your favourite color."
    #
    # my_favourite_color = request.GET['my_favourite_color']
    #
    # if my_favourite_color == 'blue':
    #     message = "The SKY is blue."
    # elif my_favourite_color == 'yellow':
    #     message = "The SUN is Yellow."

    # return HttpResponse(message)

    count_of_users = User.objects.count()

    users = User.objects.all()

    for user in users:
        print(user.name)

    context = {
        "count_of_users": count_of_users,
        "users": users
    }

    return render(request, 'users/index.html')

def signup(request):

    form = UserSignUpForm

    context = {
        'form' : form
    }
    return render(request, 'users/signup.html')
