import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Student


def health(request):
    return HttpResponse("Success", status=201)


@csrf_exempt
def add_student(request):
    """ "Add new student"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                name=data.get("name"),
                student_class=data.get("student_class"),
                age=data.get("age"),
                address=data.get("address"),
            )
            return JsonResponse(
                {"message": "student added successfully", "student_id": student.id},
                status=201,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse(
        {"message": "send a POST request with student data"}, status=100
    )


@csrf_exempt
def get_students(request):
    """Get all students"""
    if request.method == "GET":
        students = Student.objects.all().values()
        return JsonResponse(list(students), safe=False)
    return JsonResponse("error: Invalid request method", status=400)


@csrf_exempt
def get_student_by_id(request, student_id):
    """Get student by id"""
    if request.method == "GET":
        try:
            student = Student.objects.get(id=student_id)
            return JsonResponse(
                {
                    "id": student.id,
                    "name": student.name,
                    "age": student.age,
                    "address": student.address,
                }
            )
        except student.DoesNotExist:
            return JsonResponse({"error": "Student does not exist"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_student(request, student_id):
    """update students details"""
    if request.method == "PUT":
        try:
            student = Student.objects.get(id=student_id)
            print(f"Student found: {student}")

            data = json.loads(request.body)
            print(f"Received data: {data}")

            student.name = data.get("name", student.name)
            student.student_class = data.get("student_class", student.student_class)
            student.age = data.get("age", student.age)
            student.address = data.get("address", student.address)
            student.save()

            return JsonResponse({"message": "data added successfully"}, status=201)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "invalid request method"}, status=400)


@csrf_exempt
def delete_student(request, student_id):
    """Delete a student"""
    if request.method == "DELETE":
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({"message": "student deleted successfully"}, status=201)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student does not exist"}, status=4004)
    return JsonResponse({"error": "invalid request method"}, status=400)
