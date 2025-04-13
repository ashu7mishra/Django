from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import DependencySerializer

class DependencyView(APIView):
    def post(self, request):
        serializer = DependencySerializer(data=request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    