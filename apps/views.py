from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.models import App
from apps.serializers import SimpleAppSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.http import HttpRequest


class SimpleAppView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest, format=None):
        user = request.user
        apps = App.objects.filter(users=user)
        serializer = SimpleAppSerializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
