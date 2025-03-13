import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student


def print_name(request, name):
    return HttpResponse(f"name: {name}")


def add_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.object.create(
                name = data['name'],
                student_class = data['student_class'],
                age = data['age'],
                address = data['address']
            )
            return JsonResponse({'message': 'student added successfully', 'student_id': student.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({'message': 'send a POST request with student data'}, status=100)
