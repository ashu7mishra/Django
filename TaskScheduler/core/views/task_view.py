from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import TaskSerializer


class TaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
