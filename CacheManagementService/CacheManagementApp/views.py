from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.CacheManager import CacheManager

cache = CacheManager(capacity=3, strategy="LRU")


class CacheView(APIView):
    def get(self, request, key):
        value = cache.get(key)
        if not value:
            return Response(
                {"error": "Key not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response({"key": key, "value": value}, status=status.HTTP_200_OK)

    def post(self, request):
        key = request.data.get("key")
        value = request.data.get("value")
        if not key or not value:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )
        cache.put(key, value)
        return Response(
            {"message": "key added successfully"}, status=status.HTTP_201_CREATED
        )


class CacheStrategyView(APIView):
    def put(self, request):
        strategy = request.data.get("strategy")
        print(strategy)
        if strategy not in ["LRU", "LFU"]:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )
        cache.set_strategy(strategy)
        return Response(
            {"message": "Strategy updated successfully"}, status=status.HTTP_200_OK
        )
