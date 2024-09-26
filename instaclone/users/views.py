from django.shortcuts import render
from django.http import HttpResponse
from .models import User

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

    user_count = User.objects.count()

    return render(request, 'users/index.html')
