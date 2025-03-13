from django.shortcuts import render
from django.http import HttpResponse


def print_name(request):
    return HttpResponse("My name is Ashutosh")

