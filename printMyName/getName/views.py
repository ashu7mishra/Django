import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Student


def print_name(request, name):
    return HttpResponse(f"name: {name}")


@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                name = data.get('name'),
                student_class = data.get('student_class'),
                age = data.get('age'),
                address = data.get('address')
            )
            return JsonResponse({'message': 'student added successfully', 'student_id': student.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({'message': 'send a POST request with student data'}, status=100)
