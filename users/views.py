from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Profile
from users.serializers import ProfileSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class ProfileView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
